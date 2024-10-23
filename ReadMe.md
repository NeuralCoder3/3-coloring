z3  (z3-solver)
cvc5
python-mip (mip)

glucose
minisat

minizinc


https://github.com/fontanf/coloringsolver




python packages

z3-solver
mip
python-sat



https://docs.google.com/spreadsheets/d/1pq7jf-HmxQetaTUdXXNbLb5EO8KPo00qQ-ShVrr_7o0/edit?usp=sharing



TODO:

mip => unequal
gurobi
kotlin



kotlin and gradle

kotlinc test.kt -include-runtime -d tmp.jar && java -jar tmp.jar


wget https://jitpack.io/com/github/Lipen/kotlin-satlib/core/0.26.0/core-0.26.0.jar 
wget https://jitpack.io/com/github/Lipen/kotlin-satlib/jni/0.26.0/jni-0.26.0.jar


kotlinc -classpath core-0.26.0.jar:jni-0.26.0.jar test2
.kt -include-runtime -d tmp.jar

java -Djava.library.path=. -cp core-1.0.0.jar:jni-1.0.0.jar:tmp.jar MainKt
