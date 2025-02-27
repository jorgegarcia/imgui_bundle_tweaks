# Part of ImGui Bundle - MIT License - Copyright (c) 2022-2023 Pascal Thomet - https://github.com/pthom/imgui_bundle
import os

import litgen


THIS_DIR = os.path.dirname(__file__)
PYDEF_DIR = THIS_DIR
STUB_DIR = THIS_DIR + "/../../../bindings/imgui_bundle/"

CPP_HEADERS_DIR = THIS_DIR + "/../immvision/src_all_in_one/immvision"


def main():
    print("autogenerate_immvision")
    output_cpp_pydef_file = PYDEF_DIR + "/pybind_immvision.cpp"
    output_stub_pyi_file = STUB_DIR + "/immvision.pyi"

    # Configure options
    options = litgen.LitgenOptions()
    options.original_signature_flag_show = True
    options.original_location_flag_show = True
    options.namespace_root__regex = "ImmVision"
    options.srcmlcpp_options.functions_api_prefixes = "IMMVISION_API"
    options.python_run_black_formatter = True

    def post_process_stub(code: str):
        r = (
            code.replace(": cv.Mat", ": Mat")
            .replace("cv.Point2d", "Point2d")
            .replace(" = cv.Point2(", " = (")
            .replace(" = cv.Point(", " = (")
            .replace(": cv.Point", ": Point")
            .replace("cv.Matx33.eye()", "np.eye(3)")
            .replace("cv.Matx33d", "Matx33d")
            .replace("ColorMapStatsTypeId()", "ColorMapStatsTypeId.from_full_image")
            .replace("List[cv.Point]", "List[Point]")
            .replace("List[cv.Point]", "List[Point]")
            .replace("cv.Size", "Size")
            .replace("Point2d = ()", "Point2d = (0, 0)")
            .replace(" = Size()", " = (0, 0)")
        )
        return r

    options.postprocess_stub_function = post_process_stub

    generator = litgen.LitgenGenerator(options)
    generator.process_cpp_file(CPP_HEADERS_DIR + "/immvision.h")

    generator.write_generated_code(
        output_cpp_pydef_file=output_cpp_pydef_file,
        output_stub_pyi_file=output_stub_pyi_file,
    )


if __name__ == "__main__":
    main()
