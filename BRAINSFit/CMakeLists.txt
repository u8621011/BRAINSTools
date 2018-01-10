
##- project(BRAINSFit)

#-----------------------------------------------------------------------------
# Dependencies.
#

#
# ITK
#
FindITKUtil(BRAINSFit_ITK
  ITKMetricsv4
  ITKOptimizersv4
  ITKSmoothing
  ITKConnectedComponents
  ITKThresholding
  ITKImageCompare
  ITKMathematicalMorphology
  ITKBinaryMathematicalMorphology
  ITKImageLabel
  ITKRegistrationMethodsv4
  ITKDistanceMap
  ITKRegionGrowing
  ITKRegistrationCommon
  ITKTestKernel
)

if(Slicer_BUILD_I18N_SUPPORT)
  set(TS_DIR
    "${CMAKE_CURRENT_SOURCE_DIR}/Resources/Translations/"
  )

  message(STATUS "[DTC] Slicer_LANGUAGES = ${Slicer_LANGUAGES} in BRAINSFit")
  get_property(Slicer_LANGUAGES GLOBAL PROPERTY Slicer_LANGUAGES)

  set(BRAINSFit_SRCS
    BRAINSFit.cxx
    )

  set(BRAINSFit_UI_SRCS "")
  set(BRAINSFit_NAME "BRAINSFit")

  SlicerMacroTranslation(
    SRCS ${BRAINSFit_SRCS}
    UI_SRCS ${BRAINSFit_UI_SRCS}
    TS_DIR ${TS_DIR}
    TS_BASEFILENAME ${BRAINSFit_NAME}
    TS_LANGUAGES ${Slicer_LANGUAGES}
    QM_OUTPUT_DIR_VAR QM_OUTPUT_DIR
    QM_OUTPUT_FILES_VAR QM_OUTPUT_FILES
    )

  message(STATUS "[DTC] QM_OUTPUT_DIR = ${QM_OUTPUT_DIR}")
  message(STATUS "[DTC] QM_OUTPUT_FILES = ${QM_OUTPUT_FILES}")

  # what this line do?
  set_property(GLOBAL APPEND PROPERTY Slicer_QM_OUTPUT_DIRS ${QM_OUTPUT_DIR})
  message(STATUS "[DTC] Slicer_QM_OUTPUT_DIRS = ${Slicer_QM_OUTPUT_DIRS}")

  #message(STATUS "[DTC] - Adding library: ${QM_OUTPUT_FILES}")
  #message(STATUS "[DTC] - BRAINSFit var: ${BRAINSFit}")
  #add_library(${BRAINSFit}
  #  ${QM_OUTPUT_FILES}
  #  )
else()
  message(STATUS "[DTC] - BRAINSTool not aware of Slicer_BUILD_I18N_SUPPORT")
endif()

#-----------------------------------------------------------------------------
# Output directories.
#

configure_file(
  ${CMAKE_CURRENT_SOURCE_DIR}/BRAINSFitCommonLib.h.in
  ${CMAKE_CURRENT_BINARY_DIR}/BRAINSFitCommonLib.h
  )

message(STATUS "[DTC] BRAINSFit in BRAINSFit: ${BRAINSFit}")

set(ALL_PROGS_LIST
  BRAINSFit
  PerformMetricTest
  )

set(BRAINSFitLibraries BRAINSCommonLib ${ANTS_LIBS} ${BRAINSFit_ITK_LIBRARIES})
set(BRAINSFitAdditionalSources ${QM_OUTPUT_FILES})
DebugImageViewerLibAdditions(BRAINSFitLibraries)
foreach(prog ${ALL_PROGS_LIST})
  StandardBRAINSBuildMacro(NAME ${prog}
    TARGET_LIBRARIES ${BRAINSFitLibraries}
    ADDITIONAL_SRCS ${BRAINSFitAdditionalSources}
    )
endforeach()

if(BUILD_TESTING AND NOT BRAINSTools_DISABLE_TESTING)
    add_subdirectory(TestSuite)
endif()
