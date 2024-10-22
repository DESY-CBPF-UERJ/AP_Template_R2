set(ANALYSIS "AP_Template_R2")

target_sources(RunAnalysis PRIVATE ${ANALYSIS}/src/HEPHeroB.cpp ${ANALYSIS}/src/HEPRoutines.cpp ${ANALYSIS}/src/EXPTools.cpp ${ANALYSIS}/src/ANATools.cpp)
