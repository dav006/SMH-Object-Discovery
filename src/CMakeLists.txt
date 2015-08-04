set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
add_executable( make_ifs_oxfd make_ifs_oxfd)
target_link_libraries(  make_ifs_oxfd smh m)
