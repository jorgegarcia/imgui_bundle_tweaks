file(GLOB_RECURSE sources *.cpp *.h)
add_library(immapp STATIC ${sources})
if (IMGUI_BUNDLE_WITH_IMMVISION)
    target_compile_definitions(immapp PUBLIC IMGUI_BUNDLE_WITH_IMMVISION)
endif()
target_include_directories(immapp PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/..)
target_link_libraries(immapp PUBLIC hello_imgui imgui_node_editor implot imgui_md)
if (IMGUI_BUNDLE_WITH_IMFILEDIALOG)
    target_link_libraries(immapp PUBLIC im_file_dialog)
endif()
if (IMGUI_BUNDLE_WITH_TEXT_INSPECT)
    target_link_libraries(immapp PUBLIC imgui_tex_inspect)
endif()
if (IMGUI_BUNDLE_WITH_IMMVISION)
    target_link_libraries(immapp PUBLIC immvision)
endif()
target_link_libraries(imgui_bundle PUBLIC immapp)
hello_imgui_msvc_target_group_sources(immapp)
