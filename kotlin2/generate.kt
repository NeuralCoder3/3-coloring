fun main() {

    val node_count = 10000
    val edge_count = 10*node_count

    val edges =
            (0 until (node_count))
                    .flatMap { a -> (a + 1 until (node_count)).map { b -> a to b } }
                    .shuffled()
                    .take(edge_count)

    val vars =
            (0 until node_count).map({ i ->
                (0 until 3).map({ j -> i * 3 + j + 1 })
            })

    val var_count = vars.flatMap({ it }).size
    val clauses: MutableList<Array<Int>> = ArrayList()

    // for each node => at least one color
    // => or over each inner color var
    for (i in 0 until node_count) {
        val clause = vars[i].toTypedArray()
        clauses.add(clause)
    }
    // at most one color
    // => for combinations of colors => not both
    val combs = listOf(Pair(0, 1), Pair(0, 2), Pair(1, 2))
    for (i in 0 until node_count) {
        for ((j1, j2) in combs) {
            val clause = arrayOf(-vars[i][j1], -vars[i][j2])
            clauses.add(clause)
        }
    }
    // each edge not the same
    // for each edge for each node => not u or not v
    for ((u, v) in edges) {
        for (j in 0 until 3) {
            val clause = arrayOf(-vars[u][j], -vars[v][j])
            clauses.add(clause)
        }
    }

    val clause_count = clauses.size

    val file = "tmp.cnf"
    val writer = java.io.PrintWriter(file)
    writer.println("p cnf $var_count $clause_count")
    for (clause in clauses) {
        writer.println(clause.joinToString(" ") + " 0")
    }
    writer.close()



    // call glucose tmp.cnf  in glucose directory
    // keep last line of output

    // glucose or glucose.exe depending on os
    var glucose_exe = "glucose"
    if (System.getProperty("os.name").lowercase().contains("win")) {
        glucose_exe = "glucose.exe"
    }

    // run via full path
    val process = ProcessBuilder(
        // path join 
        // current working dir
        // and glucose
        System.getProperty("user.dir") + System.getProperty("file.separator") + glucose_exe,
        file
    ).start()

    val reader = java.io.BufferedReader(java.io.InputStreamReader(process.inputStream))
    process.waitFor()
    val output = reader.readLines().last()
    println(output)

}
// kotlinc test.kt -include-runtime -d test.jar && java -jar test.jar

// s SATISFIABLE
// s UNSATISFIABLE