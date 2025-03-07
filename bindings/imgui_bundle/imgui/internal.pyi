# ruff: noqa: F403, F405, B008
from typing import Any, Tuple, Optional, Callable, overload
import enum
import numpy as np

from imgui_bundle.imgui import *

##################################################
#    Manually inserted code (typedefs, etc.)
##################################################

# ErrorStringCallback represent a function that accepts a string as a single param (it will contain the error message)
ErrorStringCallback = Callable[[str], None]

# fmt: off

"""
// Use your programming IDE "Go to definition" facility on the names of the center columns to find the actual flags/enum lists.
typedef int ImGuiDataAuthority;         // -> enum ImGuiDataAuthority_      // Enum: for storing the source authority (dock node vs window) of a field
typedef int ImGuiLayoutType;            // -> enum ImGuiLayoutType_         // Enum: Horizontal or vertical
typedef int ImGuiActivateFlags;         // -> enum ImGuiActivateFlags_      // Flags: for navigation/focus function (will be for ActivateItem() later)
typedef int ImGuiDebugLogFlags;         // -> enum ImGuiDebugLogFlags_      // Flags: for ShowDebugLogWindow(), g.DebugLogFlags
typedef int ImGuiInputFlags;            // -> enum ImGuiInputFlags_         // Flags: for IsKeyPressed(), IsMouseClicked(), SetKeyOwner(), SetItemKeyOwner() etc.
typedef int ImGuiItemFlags;             // -> enum ImGuiItemFlags_          // Flags: for PushItemFlag()
typedef int ImGuiItemStatusFlags;       // -> enum ImGuiItemStatusFlags_    // Flags: for DC.LastItemStatusFlags
typedef int ImGuiOldColumnFlags;        // -> enum ImGuiOldColumnFlags_     // Flags: for BeginColumns()
typedef int ImGuiNavHighlightFlags;     // -> enum ImGuiNavHighlightFlags_  // Flags: for RenderNavHighlight()
typedef int ImGuiNavDirSourceFlags;     // -> enum ImGuiNavDirSourceFlags_  // Flags: for GetNavInputAmount2d()
typedef int ImGuiNavMoveFlags;          // -> enum ImGuiNavMoveFlags_       // Flags: for navigation requests
typedef int ImGuiNextItemDataFlags;     // -> enum ImGuiNextItemDataFlags_  // Flags: for SetNextItemXXX() functions
typedef int ImGuiNextWindowDataFlags;   // -> enum ImGuiNextWindowDataFlags_// Flags: for SetNextWindowXXX() functions
typedef int ImGuiScrollFlags;           // -> enum ImGuiScrollFlags_        // Flags: for ScrollToItem() and navigation requests
typedef int ImGuiSeparatorFlags;        // -> enum ImGuiSeparatorFlags_     // Flags: for SeparatorEx()
typedef int ImGuiTextFlags;             // -> enum ImGuiTextFlags_          // Flags: for TextEx()
typedef int ImGuiTooltipFlags;          // -> enum ImGuiTooltipFlags_       // Flags: for BeginTooltipEx()
"""
DataAuthority = int #         // -> enum DataAuthority_      // Enum: for storing the source authority (dock node vs window) of a field
LayoutType = int  #            // -> enum LayoutType_         // Enum: Horizontal or vertical
ActivateFlags = int  #         // -> enum ActivateFlags_      // Flags: for navigation/focus function (will be for ActivateItem() later)
DebugLogFlags = int  #         // -> enum DebugLogFlags_      // Flags: for ShowDebugLogWindow(), g.DebugLogFlags
InputFlags = int  #            // -> enum ImGuiInputFlags_         // Flags: for IsKeyPressed(), IsMouseClicked(), SetKeyOwner(), SetItemKeyOwner() etc.
ItemFlags = int  #             // -> enum ItemFlags_          // Flags: for PushItemFlag()
ItemStatusFlags = int  #       // -> enum ItemStatusFlags_    // Flags: for DC.LastItemStatusFlags
OldColumnFlags = int  #        // -> enum OldColumnFlags_     // Flags: for BeginColumns()
NavHighlightFlags = int  #     // -> enum NavHighlightFlags_  // Flags: for RenderNavHighlight()
NavDirSourceFlags = int  #     // -> enum NavDirSourceFlags_  // Flags: for GetNavInputAmount2d()
NavMoveFlags = int  #          // -> enum NavMoveFlags_       // Flags: for navigation requests
NextItemDataFlags = int  #     // -> enum NextItemDataFlags_  // Flags: for SetNextItemXXX() functions
NextWindowDataFlags = int  #   // -> enum NextWindowDataFlags_// Flags: for SetNextWindowXXX() functions
ScrollFlags = int  #           // -> enum ScrollFlags_        // Flags: for ScrollToItem() and navigation requests
SeparatorFlags = int  #        // -> enum SeparatorFlags_     // Flags: for SeparatorEx()
TextFlags = int  #             // -> enum TextFlags_          // Flags: for TextEx()
TooltipFlags = int  #          // -> enum TooltipFlags_       // Flags: for BeginTooltipEx()
TypingSelectFlags = int
FocusRequestFlags = int

TypingSelectFlags_None  = 0
ImFileHandle = Any

# // Our current column maximum is 64 but we may raise that in the future.
# typedef ImS8 ImGuiTableColumnIdx;
# typedef ImU8 ImGuiTableDrawChannelIdx;
TableColumnIdx = int
TableDrawChannelIdx = int
SelectionUserData = int

PopupFlags_None = PopupFlags_.none
NavHighlightFlags_TypeDefault = NavHighlightFlags_.type_default

KeyRoutingIndex = int

# Disable black formatter
# fmt: off

##################################################
#    AUTO GENERATED CODE BELOW
##################################################
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:imgui_internal.h>    ####################
# dear imgui, v1.90.0
# (internal structures/api)

# You may use this file to debug, understand or extend Dear ImGui features but we don't provide any guarantee of forward compatibility.

#
#
# Index of this file:
#
# // [SECTION] Header mess
# // [SECTION] Forward declarations
# // [SECTION] Context pointer
# // [SECTION] STB libraries includes
# // [SECTION] Macros
# // [SECTION] Generic helpers
# // [SECTION] ImDrawList support
# // [SECTION] Widgets support: flags, enums, data structures
# // [SECTION] Inputs support
# // [SECTION] Clipper support
# // [SECTION] Navigation support
# // [SECTION] Typing-select support
# // [SECTION] Columns support
# // [SECTION] Multi-select support
# // [SECTION] Docking support
# // [SECTION] Viewport support
# // [SECTION] Settings support
# // [SECTION] Localization support
# // [SECTION] Metrics, Debug tools
# // [SECTION] Generic context hooks
# // [SECTION] ImGuiContext (main imgui context)
# // [SECTION] ImGuiWindowTempData, ImGuiWindow
# // [SECTION] Tab bar, Tab item support
# // [SECTION] Table support
# // [SECTION] ImGui internal API
# // [SECTION] ImFontAtlas internal API
# // [SECTION] Test Engine specific hooks (imgui_test_engine)
#
#

# #ifndef IMGUI_DISABLE
#

# -----------------------------------------------------------------------------
# [SECTION] Header mess
# -----------------------------------------------------------------------------

#
# Adaptations for ImGui Bundle are noted with [ADAPT_IMGUI_BUNDLE]
#
# [ADAPT_IMGUI_BUNDLE]
# #ifdef IMGUI_BUNDLE_PYTHON_API
#
# #endif
#
# [/ADAPT_IMGUI_BUNDLE]

# Enable SSE intrinsics if available

# Visual Studio warnings

# Clang/GCC warnings with -Weverything

# In 1.89.4, we moved the implementation of "courtesy maths operators" from imgui_internal.h in imgui.h
# As they are frequently requested, we do not want to encourage to many people using imgui_internal.h

# Legacy defines

# Enable stb_truetype by default unless FreeType is enabled.
# You can compile with both by defining both IMGUI_ENABLE_FREETYPE and IMGUI_ENABLE_STB_TRUETYPE together.

# -----------------------------------------------------------------------------
# [SECTION] Forward declarations
# -----------------------------------------------------------------------------

# Enumerations
# Use your programming IDE "Go to definition" facility on the names of the center columns to find the actual flags/enum lists.

# Flags

# [ADAPT_IMGUI_BUNDLE]
# #ifdef IMGUI_BUNDLE_PYTHON_API
#
# #endif
#
# [/ADAPT_IMGUI_BUNDLE]

# -----------------------------------------------------------------------------
# [SECTION] Context pointer
# See implementation of this variable in imgui.cpp for comments and details.
# -----------------------------------------------------------------------------

# -------------------------------------------------------------------------
# [SECTION] STB libraries includes
# -------------------------------------------------------------------------

# namespace ImStb

# -----------------------------------------------------------------------------
# [SECTION] Macros
# -----------------------------------------------------------------------------

# Internal Drag and Drop payload types. String starting with '_' are reserved for Dear ImGui.

# Debug Printing Into TTY
# (since IMGUI_VERSION_NUM >= 18729: IMGUI_DEBUG_LOG was reworked into IMGUI_DEBUG_PRINTF (and removed framecount from it). If you were using a #define IMGUI_DEBUG_LOG please rename)

# Debug Logging for ShowDebugLogWindow(). This is designed for relatively rare events so please don't spam.

# "Paranoid" Debug Asserts are meant to only be enabled during specific debugging/work, otherwise would slow down the code too much.
# We currently don't have many of those so the effect is currently negligible, but onward intent to add more aggressive ones in the code.
##define IMGUI_DEBUG_PARANOID

# Error handling
# Down the line in some frameworks/languages we would like to have a way to redirect those to the programmer and recover from more faults.

# Enforce cdecl calling convention for functions called by the standard library, in case compilation settings changed the default to e.g. __vectorcall

# Warnings

# Debug Tools
# Use 'Metrics/Debugger->Tools->Item Picker' to break into the call-stack of a specific item.
# This will call IM_DEBUG_BREAK() which you may redefine yourself. See https://github.com/scottt/debugbreak for more reference.

# Format specifiers, printing 64-bit hasn't been decently standardized...
# In a real application you should be using PRId64 and PRIu64 from <inttypes.h> (non-windows) and on Windows define them yourself.

# -----------------------------------------------------------------------------
# [SECTION] Generic helpers
# Note that the ImXXX helpers functions are lower-level than ImGui functions.
# ImGui functions or the ImGui context are never called/used from other ImXXX functions.
# -----------------------------------------------------------------------------
# - Helpers: Hashing
# - Helpers: Sorting
# - Helpers: Bit manipulation
# - Helpers: String
# - Helpers: Formatting
# - Helpers: UTF-8 <> wchar conversions
# - Helpers: ImVec2/ImVec4 operators
# - Helpers: Maths
# - Helpers: Geometry
# - Helper: ImVec1
# - Helper: ImVec2ih
# - Helper: ImRect
# - Helper: ImBitArray
# - Helper: ImBitVector
# - Helper: ImSpan<>, ImSpanAllocator<>
# - Helper: ImPool<>
# - Helper: ImChunkStream<>
# - Helper: ImGuiTextIndex
# -----------------------------------------------------------------------------

# Helpers: Hashing
# IMGUI_API ImGuiID       ImHashData(const void* data, size_t data_size, ImGuiID seed = 0);    /* original C++ signature */
def im_hash_data(data: Any, data_size: int, seed: ID = 0) -> ID:
    pass

# IMGUI_API ImGuiID       ImHashStr(const char* data, size_t data_size = 0, ImGuiID seed = 0);    /* original C++ signature */
def im_hash_str(data: str, data_size: int = 0, seed: ID = 0) -> ID:
    pass

# Helpers: Sorting

# IMGUI_API ImU32         ImAlphaBlendColors(ImU32 col_a, ImU32 col_b);    /* original C++ signature */
def im_alpha_blend_colors(col_a: ImU32, col_b: ImU32) -> ImU32:
    """Helpers: Color Blending"""
    pass

# Helpers: Bit manipulation
# static inline bool      ImIsPowerOfTwo(int v)           { return v != 0 && (v & (v - 1)) == 0; }    /* original C++ signature */
@overload
def im_is_power_of_two(v: int) -> bool:
    """(private API)"""
    pass

# static inline bool      ImIsPowerOfTwo(ImU64 v)         { return v != 0 && (v & (v - 1)) == 0; }    /* original C++ signature */
@overload
def im_is_power_of_two(v: ImU64) -> bool:
    """(private API)"""
    pass

# static inline int       ImUpperPowerOfTwo(int v)        { v--; v |= v >> 1; v |= v >> 2; v |= v >> 4; v |= v >> 8; v |= v >> 16; v++; return v; }    /* original C++ signature */
def im_upper_power_of_two(v: int) -> int:
    """(private API)"""
    pass

# Helpers: String
# static inline bool      ImCharIsBlankW(unsigned int c)  { return c == ' ' || c == '\t' || c == 0x3000; }    /* original C++ signature */
def im_char_is_blank_w(c: int) -> bool:
    """(private API)"""
    pass

# Helpers: Formatting

# Helpers: UTF-8 <> wchar conversions
# IMGUI_API const char*   ImTextFindPreviousUtf8Codepoint(const char* in_text_start, const char* in_text_curr);                       /* original C++ signature */
def im_text_find_previous_utf8_codepoint(in_text_start: str, in_text_curr: str) -> str:
    pass

# return previous UTF-8 code-point.

# Helpers: File System

# - Wrapper for standard libs functions. (Note that imgui_demo.cpp does _not_ use them to keep the code easy to copy)
# - ImMin/ImMax/ImClamp/ImLerp/ImSwap are used by widgets which support variety of types: signed/unsigned int/long long float/double
# (Exceptionally using templates here but we could also redefine them for those types)
# - Misc maths helpers
# static inline ImVec2 ImMin(const ImVec2& lhs, const ImVec2& rhs)                { return ImVec2(lhs.x < rhs.x ? lhs.x : rhs.x, lhs.y < rhs.y ? lhs.y : rhs.y); }    /* original C++ signature */
@overload
def im_min(lhs: ImVec2, rhs: ImVec2) -> ImVec2:
    """(private API)"""
    pass

# static inline ImVec2 ImMax(const ImVec2& lhs, const ImVec2& rhs)                { return ImVec2(lhs.x >= rhs.x ? lhs.x : rhs.x, lhs.y >= rhs.y ? lhs.y : rhs.y); }    /* original C++ signature */
@overload
def im_max(lhs: ImVec2, rhs: ImVec2) -> ImVec2:
    """(private API)"""
    pass

# static inline ImVec2 ImClamp(const ImVec2& v, const ImVec2& mn, ImVec2 mx)      { return ImVec2((v.x < mn.x) ? mn.x : (v.x > mx.x) ? mx.x : v.x, (v.y < mn.y) ? mn.y : (v.y > mx.y) ? mx.y : v.y); }    /* original C++ signature */
@overload
def im_clamp(v: ImVec2, mn: ImVec2, mx: ImVec2) -> ImVec2:
    """(private API)"""
    pass

# static inline ImVec2 ImLerp(const ImVec2& a, const ImVec2& b, float t)          { return ImVec2(a.x + (b.x - a.x) * t, a.y + (b.y - a.y) * t); }    /* original C++ signature */
@overload
def im_lerp(a: ImVec2, b: ImVec2, t: float) -> ImVec2:
    """(private API)"""
    pass

# static inline ImVec2 ImLerp(const ImVec2& a, const ImVec2& b, const ImVec2& t)  { return ImVec2(a.x + (b.x - a.x) * t.x, a.y + (b.y - a.y) * t.y); }    /* original C++ signature */
@overload
def im_lerp(a: ImVec2, b: ImVec2, t: ImVec2) -> ImVec2:
    """(private API)"""
    pass

# static inline ImVec4 ImLerp(const ImVec4& a, const ImVec4& b, float t)          { return ImVec4(a.x + (b.x - a.x) * t, a.y + (b.y - a.y) * t, a.z + (b.z - a.z) * t, a.w + (b.w - a.w) * t); }    /* original C++ signature */
@overload
def im_lerp(a: ImVec4, b: ImVec4, t: float) -> ImVec4:
    """(private API)"""
    pass

# static inline float  ImSaturate(float f)                                        { return (f < 0.0f) ? 0.0f : (f > 1.0f) ? 1.0f : f; }    /* original C++ signature */
def im_saturate(f: float) -> float:
    """(private API)"""
    pass

# static inline float  ImLengthSqr(const ImVec2& lhs)                             { return (lhs.x * lhs.x) + (lhs.y * lhs.y); }    /* original C++ signature */
@overload
def im_length_sqr(lhs: ImVec2) -> float:
    """(private API)"""
    pass

# static inline float  ImLengthSqr(const ImVec4& lhs)                             { return (lhs.x * lhs.x) + (lhs.y * lhs.y) + (lhs.z * lhs.z) + (lhs.w * lhs.w); }    /* original C++ signature */
@overload
def im_length_sqr(lhs: ImVec4) -> float:
    """(private API)"""
    pass

# static inline float  ImInvLength(const ImVec2& lhs, float fail_value)           { float d = (lhs.x * lhs.x) + (lhs.y * lhs.y); if (d > 0.0f) return ImRsqrt(d); return fail_value; }    /* original C++ signature */
def im_inv_length(lhs: ImVec2, fail_value: float) -> float:
    """(private API)"""
    pass

# static inline float  ImTrunc(float f)                                           { return (float)(int)(f); }    /* original C++ signature */
@overload
def im_trunc(f: float) -> float:
    """(private API)"""
    pass

# static inline ImVec2 ImTrunc(const ImVec2& v)                                   { return ImVec2((float)(int)(v.x), (float)(int)(v.y)); }    /* original C++ signature */
@overload
def im_trunc(v: ImVec2) -> ImVec2:
    """(private API)"""
    pass

# static inline float  ImFloor(float f)                                           { return (float)((f >= 0 || (float)(int)f == f) ? (int)f : (int)f - 1); }     /* original C++ signature */
@overload
def im_floor(f: float) -> float:
    """(private API)

    Decent replacement for floorf()
    """
    pass

# static inline ImVec2 ImFloor(const ImVec2& v)                                   { return ImVec2(ImFloor(v.x), ImFloor(v.y)); }    /* original C++ signature */
@overload
def im_floor(v: ImVec2) -> ImVec2:
    """(private API)"""
    pass

# static inline int    ImModPositive(int a, int b)                                { return (a + b) % b; }    /* original C++ signature */
def im_mod_positive(a: int, b: int) -> int:
    """(private API)"""
    pass

# static inline float  ImDot(const ImVec2& a, const ImVec2& b)                    { return a.x * b.x + a.y * b.y; }    /* original C++ signature */
def im_dot(a: ImVec2, b: ImVec2) -> float:
    """(private API)"""
    pass

# static inline ImVec2 ImRotate(const ImVec2& v, float cos_a, float sin_a)        { return ImVec2(v.x * cos_a - v.y * sin_a, v.x * sin_a + v.y * cos_a); }    /* original C++ signature */
def im_rotate(v: ImVec2, cos_a: float, sin_a: float) -> ImVec2:
    """(private API)"""
    pass

# static inline float  ImLinearSweep(float current, float target, float speed)    { if (current < target) return ImMin(current + speed, target); if (current > target) return ImMax(current - speed, target); return current; }    /* original C++ signature */
def im_linear_sweep(current: float, target: float, speed: float) -> float:
    """(private API)"""
    pass

# static inline ImVec2 ImMul(const ImVec2& lhs, const ImVec2& rhs)                { return ImVec2(lhs.x * rhs.x, lhs.y * rhs.y); }    /* original C++ signature */
def im_mul(lhs: ImVec2, rhs: ImVec2) -> ImVec2:
    """(private API)"""
    pass

# static inline bool   ImIsFloatAboveGuaranteedIntegerPrecision(float f)          { return f <= -16777216 || f >= 16777216; }    /* original C++ signature */
def im_is_float_above_guaranteed_integer_precision(f: float) -> bool:
    """(private API)"""
    pass

# static inline float  ImExponentialMovingAverage(float avg, float sample, int n) { avg -= avg / n; avg += sample / n; return avg; }    /* original C++ signature */
def im_exponential_moving_average(avg: float, sample: float, n: int) -> float:
    """(private API)"""
    pass

# Helpers: Geometry
# IMGUI_API ImVec2     ImBezierCubicCalc(const ImVec2& p1, const ImVec2& p2, const ImVec2& p3, const ImVec2& p4, float t);    /* original C++ signature */
def im_bezier_cubic_calc(
    p1: ImVec2, p2: ImVec2, p3: ImVec2, p4: ImVec2, t: float
) -> ImVec2:
    pass

# IMGUI_API ImVec2     ImBezierCubicClosestPoint(const ImVec2& p1, const ImVec2& p2, const ImVec2& p3, const ImVec2& p4, const ImVec2& p, int num_segments);           /* original C++ signature */
def im_bezier_cubic_closest_point(
    p1: ImVec2, p2: ImVec2, p3: ImVec2, p4: ImVec2, p: ImVec2, num_segments: int
) -> ImVec2:
    """For curves with explicit number of segments"""
    pass

# IMGUI_API ImVec2     ImBezierCubicClosestPointCasteljau(const ImVec2& p1, const ImVec2& p2, const ImVec2& p3, const ImVec2& p4, const ImVec2& p, float tess_tol);    /* original C++ signature */
def im_bezier_cubic_closest_point_casteljau(
    p1: ImVec2, p2: ImVec2, p3: ImVec2, p4: ImVec2, p: ImVec2, tess_tol: float
) -> ImVec2:
    """For auto-tessellated curves you can use tess_tol = style.CurveTessellationTol"""
    pass

# IMGUI_API ImVec2     ImBezierQuadraticCalc(const ImVec2& p1, const ImVec2& p2, const ImVec2& p3, float t);    /* original C++ signature */
def im_bezier_quadratic_calc(p1: ImVec2, p2: ImVec2, p3: ImVec2, t: float) -> ImVec2:
    pass

# IMGUI_API ImVec2     ImLineClosestPoint(const ImVec2& a, const ImVec2& b, const ImVec2& p);    /* original C++ signature */
def im_line_closest_point(a: ImVec2, b: ImVec2, p: ImVec2) -> ImVec2:
    pass

# IMGUI_API bool       ImTriangleContainsPoint(const ImVec2& a, const ImVec2& b, const ImVec2& c, const ImVec2& p);    /* original C++ signature */
def im_triangle_contains_point(a: ImVec2, b: ImVec2, c: ImVec2, p: ImVec2) -> bool:
    pass

# IMGUI_API ImVec2     ImTriangleClosestPoint(const ImVec2& a, const ImVec2& b, const ImVec2& c, const ImVec2& p);    /* original C++ signature */
def im_triangle_closest_point(a: ImVec2, b: ImVec2, c: ImVec2, p: ImVec2) -> ImVec2:
    pass

# IMGUI_API void       ImTriangleBarycentricCoords(const ImVec2& a, const ImVec2& b, const ImVec2& c, const ImVec2& p, float& out_u, float& out_v, float& out_w);    /* original C++ signature */
def im_triangle_barycentric_coords(
    a: ImVec2, b: ImVec2, c: ImVec2, p: ImVec2, out_u: float, out_v: float, out_w: float
) -> Tuple[float, float, float]:
    pass

# inline float         ImTriangleArea(const ImVec2& a, const ImVec2& b, const ImVec2& c) { return ImFabs((a.x * (b.y - c.y)) + (b.x * (c.y - a.y)) + (c.x * (a.y - b.y))) * 0.5f; }    /* original C++ signature */
def im_triangle_area(a: ImVec2, b: ImVec2, c: ImVec2) -> float:
    """(private API)"""
    pass

class ImVec1:
    # float   x;    /* original C++ signature */
    x: float
    # constexpr ImVec1()         : x(0.0f) { }    /* original C++ signature */
    @overload
    def __init__(self) -> None:
        pass
    # constexpr ImVec1(float _x) : x(_x) { }    /* original C++ signature */
    @overload
    def __init__(self, _x: float) -> None:
        pass

class ImVec2ih:
    """Helper: ImVec2ih (2D vector, half-size integer, for long-term packed storage)"""

    # short   x,     /* original C++ signature */
    x: int
    # y;    /* original C++ signature */
    y: int
    # constexpr ImVec2ih()                           : x(0), y(0) {}    /* original C++ signature */
    @overload
    def __init__(self) -> None:
        pass
    # constexpr ImVec2ih(short _x, short _y)         : x(_x), y(_y) {}    /* original C++ signature */
    @overload
    def __init__(self, _x: int, _y: int) -> None:
        pass
    # constexpr explicit ImVec2ih(const ImVec2& rhs) : x((short)rhs.x), y((short)rhs.y) {}    /* original C++ signature */
    @overload
    def __init__(self, rhs: ImVec2) -> None:
        pass

class ImRect:
    """Helper: ImRect (2D axis aligned bounding-box)
    NB: we can't rely on ImVec2 math operators being available here!
    """

    # ImVec2      Min;    /* original C++ signature */
    min: ImVec2  # Upper-left
    # ImVec2      Max;    /* original C++ signature */
    max: ImVec2  # Lower-right

    # constexpr ImRect()                                        : Min(0.0f, 0.0f), Max(0.0f, 0.0f)  {}    /* original C++ signature */
    @overload
    def __init__(self) -> None:
        pass
    # constexpr ImRect(const ImVec2& min, const ImVec2& max)    : Min(min), Max(max)                {}    /* original C++ signature */
    @overload
    def __init__(self, min: ImVec2, max: ImVec2) -> None:
        pass
    # constexpr ImRect(const ImVec4& v)                         : Min(v.x, v.y), Max(v.z, v.w)      {}    /* original C++ signature */
    @overload
    def __init__(self, v: ImVec4) -> None:
        pass
    # constexpr ImRect(float x1, float y1, float x2, float y2)  : Min(x1, y1), Max(x2, y2)          {}    /* original C++ signature */
    @overload
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        pass
    # ImVec2      GetCenter() const                   { return ImVec2((Min.x + Max.x) * 0.5f, (Min.y + Max.y) * 0.5f); }    /* original C++ signature */
    def get_center(self) -> ImVec2:
        """(private API)"""
        pass
    # ImVec2      GetSize() const                     { return ImVec2(Max.x - Min.x, Max.y - Min.y); }    /* original C++ signature */
    def get_size(self) -> ImVec2:
        """(private API)"""
        pass
    # float       GetWidth() const                    { return Max.x - Min.x; }    /* original C++ signature */
    def get_width(self) -> float:
        """(private API)"""
        pass
    # float       GetHeight() const                   { return Max.y - Min.y; }    /* original C++ signature */
    def get_height(self) -> float:
        """(private API)"""
        pass
    # float       GetArea() const                     { return (Max.x - Min.x) * (Max.y - Min.y); }    /* original C++ signature */
    def get_area(self) -> float:
        """(private API)"""
        pass
    # ImVec2      GetTL() const                       { return Min; }                       /* original C++ signature */
    def get_tl(self) -> ImVec2:
        """(private API)

        Top-left
        """
        pass
    # ImVec2      GetTR() const                       { return ImVec2(Max.x, Min.y); }      /* original C++ signature */
    def get_tr(self) -> ImVec2:
        """(private API)

        Top-right
        """
        pass
    # ImVec2      GetBL() const                       { return ImVec2(Min.x, Max.y); }      /* original C++ signature */
    def get_bl(self) -> ImVec2:
        """(private API)

        Bottom-left
        """
        pass
    # ImVec2      GetBR() const                       { return Max; }                       /* original C++ signature */
    def get_br(self) -> ImVec2:
        """(private API)

        Bottom-right
        """
        pass
    # bool        Contains(const ImVec2& p) const     { return p.x     >= Min.x && p.y     >= Min.y && p.x     <  Max.x && p.y     <  Max.y; }    /* original C++ signature */
    @overload
    def contains(self, p: ImVec2) -> bool:
        """(private API)"""
        pass
    # bool        Contains(const ImRect& r) const     { return r.Min.x >= Min.x && r.Min.y >= Min.y && r.Max.x <= Max.x && r.Max.y <= Max.y; }    /* original C++ signature */
    @overload
    def contains(self, r: ImRect) -> bool:
        """(private API)"""
        pass
    # bool        ContainsWithPad(const ImVec2& p, const ImVec2& pad) const { return p.x >= Min.x - pad.x && p.y >= Min.y - pad.y && p.x < Max.x + pad.x && p.y < Max.y + pad.y; }    /* original C++ signature */
    def contains_with_pad(self, p: ImVec2, pad: ImVec2) -> bool:
        """(private API)"""
        pass
    # bool        Overlaps(const ImRect& r) const     { return r.Min.y <  Max.y && r.Max.y >  Min.y && r.Min.x <  Max.x && r.Max.x >  Min.x; }    /* original C++ signature */
    def overlaps(self, r: ImRect) -> bool:
        """(private API)"""
        pass
    # void        Add(const ImVec2& p)                { if (Min.x > p.x)     Min.x = p.x;     if (Min.y > p.y)     Min.y = p.y;     if (Max.x < p.x)     Max.x = p.x;     if (Max.y < p.y)     Max.y = p.y; }    /* original C++ signature */
    @overload
    def add(self, p: ImVec2) -> None:
        """(private API)"""
        pass
    # void        Add(const ImRect& r)                { if (Min.x > r.Min.x) Min.x = r.Min.x; if (Min.y > r.Min.y) Min.y = r.Min.y; if (Max.x < r.Max.x) Max.x = r.Max.x; if (Max.y < r.Max.y) Max.y = r.Max.y; }    /* original C++ signature */
    @overload
    def add(self, r: ImRect) -> None:
        """(private API)"""
        pass
    # void        Expand(const float amount)          { Min.x -= amount;   Min.y -= amount;   Max.x += amount;   Max.y += amount; }    /* original C++ signature */
    @overload
    def expand(self, amount: float) -> None:
        """(private API)"""
        pass
    # void        Expand(const ImVec2& amount)        { Min.x -= amount.x; Min.y -= amount.y; Max.x += amount.x; Max.y += amount.y; }    /* original C++ signature */
    @overload
    def expand(self, amount: ImVec2) -> None:
        """(private API)"""
        pass
    # void        Translate(const ImVec2& d)          { Min.x += d.x; Min.y += d.y; Max.x += d.x; Max.y += d.y; }    /* original C++ signature */
    def translate(self, d: ImVec2) -> None:
        """(private API)"""
        pass
    # void        TranslateX(float dx)                { Min.x += dx; Max.x += dx; }    /* original C++ signature */
    def translate_x(self, dx: float) -> None:
        """(private API)"""
        pass
    # void        TranslateY(float dy)                { Min.y += dy; Max.y += dy; }    /* original C++ signature */
    def translate_y(self, dy: float) -> None:
        """(private API)"""
        pass
    # void        ClipWith(const ImRect& r)           { Min = ImMax(Min, r.Min); Max = ImMin(Max, r.Max); }                       /* original C++ signature */
    def clip_with(self, r: ImRect) -> None:
        """(private API)

        Simple version, may lead to an inverted rectangle, which is fine for Contains/Overlaps test but not for display.
        """
        pass
    # void        ClipWithFull(const ImRect& r)       { Min = ImClamp(Min, r.Min, r.Max); Max = ImClamp(Max, r.Min, r.Max); }     /* original C++ signature */
    def clip_with_full(self, r: ImRect) -> None:
        """(private API)

        Full version, ensure both points are fully clipped.
        """
        pass
    # void        Floor()                             { Min.x = IM_TRUNC(Min.x); Min.y = IM_TRUNC(Min.y); Max.x = IM_TRUNC(Max.x); Max.y = IM_TRUNC(Max.y); }    /* original C++ signature */
    def floor(self) -> None:
        """(private API)"""
        pass
    # bool        IsInverted() const                  { return Min.x > Max.x || Min.y > Max.y; }    /* original C++ signature */
    def is_inverted(self) -> bool:
        """(private API)"""
        pass
    # ImVec4      ToVec4() const                      { return ImVec4(Min.x, Min.y, Max.x, Max.y); }    /* original C++ signature */
    def to_vec4(self) -> ImVec4:
        """(private API)"""
        pass

# Helper: ImBitArray
# inline size_t   ImBitArrayGetStorageSizeInBytes(int bitcount)   { return (size_t)((bitcount + 31) >> 5) << 2; }    /* original C++ signature */
def im_bit_array_get_storage_size_in_bytes(bitcount: int) -> int:
    """(private API)"""
    pass

# inline void     ImBitArrayClearAllBits(ImU32* arr, int bitcount){ memset(arr, 0, ImBitArrayGetStorageSizeInBytes(bitcount)); }    /* original C++ signature */
def im_bit_array_clear_all_bits(arr: ImU32, bitcount: int) -> None:
    """(private API)"""
    pass

# inline bool     ImBitArrayTestBit(const ImU32* arr, int n)      { ImU32 mask = (ImU32)1 << (n & 31); return (arr[n >> 5] & mask) != 0; }    /* original C++ signature */
def im_bit_array_test_bit(arr: ImU32, n: int) -> bool:
    """(private API)"""
    pass

# inline void     ImBitArrayClearBit(ImU32* arr, int n)           { ImU32 mask = (ImU32)1 << (n & 31); arr[n >> 5] &= ~mask; }    /* original C++ signature */
def im_bit_array_clear_bit(arr: ImU32, n: int) -> None:
    """(private API)"""
    pass

# inline void     ImBitArraySetBit(ImU32* arr, int n)             { ImU32 mask = (ImU32)1 << (n & 31); arr[n >> 5] |= mask; }    /* original C++ signature */
def im_bit_array_set_bit(arr: ImU32, n: int) -> None:
    """(private API)"""
    pass

# inline void     ImBitArraySetBitRange(ImU32* arr, int n, int n2) // Works on range [n..n2)    /* original C++ signature */
# {
#     n2--;
#     while (n <= n2)
#     {
#         int a_mod = (n & 31);
#         int b_mod = (n2 > (n | 31) ? 31 : (n2 & 31)) + 1;
#         ImU32 mask = (ImU32)(((ImU64)1 << b_mod) - 1) & ~(ImU32)(((ImU64)1 << a_mod) - 1);
#         arr[n >> 5] |= mask;
#         n = (n + 32) & ~31;
#     }
# }
def im_bit_array_set_bit_range(arr: ImU32, n: int, n2: int) -> None:
    """(private API)

    // Works on range [n..n2)
    """
    pass

class ImBitVector:
    """Helper: ImBitVector
    Store 1-bit per value.
    """

    # ImVector<ImU32> Storage;    /* original C++ signature */
    storage: ImVector_ImU32
    # void            Create(int sz)              { Storage.resize((sz + 31) >> 5); memset(Storage.Data, 0, (size_t)Storage.Size * sizeof(Storage.Data[0])); }    /* original C++ signature */
    def create(self, sz: int) -> None:
        """(private API)"""
        pass
    # void            Clear()                     { Storage.clear(); }    /* original C++ signature */
    def clear(self) -> None:
        """(private API)"""
        pass
    # bool            TestBit(int n) const        { IM_ASSERT(n < (Storage.Size << 5)); return IM_BITARRAY_TESTBIT(Storage.Data, n); }    /* original C++ signature */
    def test_bit(self, n: int) -> bool:
        """(private API)"""
        pass
    # void            SetBit(int n)               { IM_ASSERT(n < (Storage.Size << 5)); ImBitArraySetBit(Storage.Data, n); }    /* original C++ signature */
    def set_bit(self, n: int) -> None:
        """(private API)"""
        pass
    # void            ClearBit(int n)             { IM_ASSERT(n < (Storage.Size << 5)); ImBitArrayClearBit(Storage.Data, n); }    /* original C++ signature */
    def clear_bit(self, n: int) -> None:
        """(private API)"""
        pass
    # ImBitVector(ImVector<ImU32> Storage = ImVector<ImU32>());    /* original C++ signature */
    def __init__(self, storage: ImVector_ImU32 = ImVector_ImU32()) -> None:
        """Auto-generated default constructor with named params"""
        pass

class TextIndex:
    """Helper: ImGuiTextIndex<>
    Maintain a line index for a text buffer. This is a strong candidate to be moved into the public API.
    """

    # ImVector<int>   LineOffsets;    /* original C++ signature */
    line_offsets: ImVector_int
    # int             EndOffset = 0;    /* original C++ signature */
    end_offset: int = 0  # Because we don't own text buffer we need to maintain EndOffset (may bake in LineOffsets?)

    # void            clear()                                 { LineOffsets.clear(); EndOffset = 0; }    /* original C++ signature */
    def clear(self) -> None:
        """(private API)"""
        pass
    # int             size()                                  { return LineOffsets.Size; }    /* original C++ signature */
    def size(self) -> int:
        """(private API)"""
        pass
    # const char*     get_line_begin(const char* base, int n) { return base + LineOffsets[n]; }    /* original C++ signature */
    def get_line_begin(self, base: str, n: int) -> str:
        """(private API)"""
        pass
    # const char*     get_line_end(const char* base, int n)   { return base + (n + 1 < LineOffsets.Size ? (LineOffsets[n + 1] - 1) : EndOffset); }    /* original C++ signature */
    def get_line_end(self, base: str, n: int) -> str:
        """(private API)"""
        pass
    # void            append(const char* base, int old_size, int new_size);    /* original C++ signature */
    def append(self, base: str, old_size: int, new_size: int) -> None:
        """(private API)"""
        pass
    # ImGuiTextIndex(ImVector<int> LineOffsets = ImVector<int>(), int EndOffset = 0);    /* original C++ signature */
    def __init__(
        self, line_offsets: ImVector_int = ImVector_int(), end_offset: int = 0
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

# -----------------------------------------------------------------------------
# [SECTION] ImDrawList support
# -----------------------------------------------------------------------------

# ImDrawList: Helper function to calculate a circle's segment count given its radius and a "maximum error" value.
# Estimation of number of circle segment based on error is derived using method described in https://stackoverflow.com/a/2244088/15194693
# Number of segments (N) is calculated using equation:
#   N = ceil ( pi / acos(1 - error / r) )     where r > 0, error <= r
# Our equation is significantly simpler that one in the post thanks for choosing segment that is
# perpendicular to X axis. Follow steps in the article from this starting condition and you will
# will get this result.
#
# Rendering circles with an odd number of segments, while mathematically correct will produce
# asymmetrical results on the raster grid. Therefore we're rounding N to next even number (7->8, 8->8, 9->10 etc.)

# Raw equation from IM_DRAWLIST_CIRCLE_AUTO_SEGMENT_CALC rewritten for 'r' and 'error'.

# ImDrawList: Lookup table size for adaptive arc drawing, cover full circle.

class ImDrawListSharedData:
    """Data shared between all ImDrawList instances
    You may want to create your own instance of this if you want to use ImDrawList completely without ImGui. In that case, watch out for future changes to this structure.
    """

    # ImVec2          TexUvWhitePixel;    /* original C++ signature */
    tex_uv_white_pixel: ImVec2  # UV of white pixel in the atlas
    # ImFont*         Font;    /* original C++ signature */
    font: ImFont  # Current/default font (optional, for simplified AddText overload)
    # float           FontSize;    /* original C++ signature */
    font_size: float  # Current/default font size (optional, for simplified AddText overload)
    # float           CurveTessellationTol;    /* original C++ signature */
    curve_tessellation_tol: float  # Tessellation tolerance when using PathBezierCurveTo()
    # float           CircleSegmentMaxError;    /* original C++ signature */
    circle_segment_max_error: float  # Number of circle segments to use per pixel of radius for AddCircle() etc
    # ImVec4          ClipRectFullscreen;    /* original C++ signature */
    clip_rect_fullscreen: ImVec4  # Value for PushClipRectFullscreen()
    # ImDrawListFlags InitialFlags;    /* original C++ signature */
    initial_flags: ImDrawListFlags  # Initial flags at the beginning of the frame (it is possible to alter flags on a per-drawlist basis afterwards)

    # ImVector<ImVec2> TempBuffer;    /* original C++ signature */
    # [Internal] Temp write buffer
    temp_buffer: ImVector_ImVec2

    # [Internal] Lookup tables
    # float           ArcFastRadiusCutoff;    /* original C++ signature */
    arc_fast_radius_cutoff: float  # Cutoff radius after which arc drawing will fallback to slower PathArcTo()
    # ImU8            CircleSegmentCounts[64];    /* original C++ signature */
    circle_segment_counts: np.ndarray  # ndarray[type=ImU8, size=64]  # Precomputed segment count for given radius before we calculate it dynamically (to avoid calculation overhead)
    # const ImVec4*   TexUvLines;    /* original C++ signature */
    tex_uv_lines: ImVec4  # UV of anti-aliased lines in the atlas # (const)

    # ImDrawListSharedData();    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # void SetCircleTessellationMaxError(float max_error);    /* original C++ signature */
    def set_circle_tessellation_max_error(self, max_error: float) -> None:
        """(private API)"""
        pass

class ImDrawDataBuilder:
    # ImVector<ImDrawList*>   LayerData1;    /* original C++ signature */
    layer_data1: ImVector_ImDrawList_ptr

    # ImDrawDataBuilder()                     { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

# -----------------------------------------------------------------------------
# [SECTION] Widgets support: flags, enums, data structures
# -----------------------------------------------------------------------------

class ItemFlags_(enum.Enum):
    """Flags used by upcoming items
    - input: PushItemFlag() manipulates g.CurrentItemFlags, ItemAdd() calls may add extra flags.
    - output: stored in g.LastItemData.InFlags
    Current window shared by all windows.
    This is going to be exposed in imgui.h when stabilized enough.
    """

    # Controlled by user
    # ImGuiItemFlags_None                     = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiItemFlags_NoTabStop                = 1 << 0,      /* original C++ signature */
    no_tab_stop = (
        enum.auto()
    )  # (= 1 << 0)  # False     // Disable keyboard tabbing. This is a "lighter" version of ImGuiItemFlags_NoNav.
    # ImGuiItemFlags_ButtonRepeat             = 1 << 1,      /* original C++ signature */
    button_repeat = (
        enum.auto()
    )  # (= 1 << 1)  # False     // Button() will return True multiple times based on io.KeyRepeatDelay and io.KeyRepeatRate settings.
    # ImGuiItemFlags_Disabled                 = 1 << 2,      /* original C++ signature */
    disabled = (
        enum.auto()
    )  # (= 1 << 2)  # False     // Disable interactions but doesn't affect visuals. See BeginDisabled()/EndDisabled(). See github.com/ocornut/imgui/issues/211
    # ImGuiItemFlags_NoNav                    = 1 << 3,      /* original C++ signature */
    no_nav = (
        enum.auto()
    )  # (= 1 << 3)  # False     // Disable any form of focusing (keyboard/gamepad directional navigation and SetKeyboardFocusHere() calls)
    # ImGuiItemFlags_NoNavDefaultFocus        = 1 << 4,      /* original C++ signature */
    no_nav_default_focus = (
        enum.auto()
    )  # (= 1 << 4)  # False     // Disable item being a candidate for default focus (e.g. used by title bar items)
    # ImGuiItemFlags_SelectableDontClosePopup = 1 << 5,      /* original C++ signature */
    selectable_dont_close_popup = (
        enum.auto()
    )  # (= 1 << 5)  # False     // Disable MenuItem/Selectable() automatically closing their popup window
    # ImGuiItemFlags_MixedValue               = 1 << 6,      /* original C++ signature */
    mixed_value = (
        enum.auto()
    )  # (= 1 << 6)  # False     // [BETA] Represent a mixed/indeterminate value, generally multi-selection where values differ. Currently only supported by Checkbox() (later should support all sorts of widgets)
    # ImGuiItemFlags_ReadOnly                 = 1 << 7,      /* original C++ signature */
    read_only = (
        enum.auto()
    )  # (= 1 << 7)  # False     // [ALPHA] Allow hovering interactions but underlying value is not changed.
    # ImGuiItemFlags_NoWindowHoverableCheck   = 1 << 8,      /* original C++ signature */
    no_window_hoverable_check = (
        enum.auto()
    )  # (= 1 << 8)  # False     // Disable hoverable check in ItemHoverable()
    # ImGuiItemFlags_AllowOverlap             = 1 << 9,      /* original C++ signature */
    allow_overlap = (
        enum.auto()
    )  # (= 1 << 9)  # False     // Allow being overlapped by another widget. Not-hovered to Hovered transition deferred by a frame.

    # Controlled by widget code
    # ImGuiItemFlags_Inputable                = 1 << 10,     /* original C++ signature */
    inputable = (
        enum.auto()
    )  # (= 1 << 10)  # False     // [WIP] Auto-activate input mode when tab focused. Currently only used and supported by a few items before it becomes a generic feature.
    # ImGuiItemFlags_HasSelectionUserData     = 1 << 11,     /* original C++ signature */
    has_selection_user_data = (
        enum.auto()
    )  # (= 1 << 11)  # False     // Set by SetNextItemSelectionUserData()

class ItemStatusFlags_(enum.Enum):
    """Status flags for an already submitted item
    - output: stored in g.LastItemData.StatusFlags
    """

    # ImGuiItemStatusFlags_None               = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiItemStatusFlags_HoveredRect        = 1 << 0,       /* original C++ signature */
    hovered_rect = (
        enum.auto()
    )  # (= 1 << 0)  # Mouse position is within item rectangle (does NOT mean that the window is in correct z-order and can be hovered!, this is only one part of the most-common IsItemHovered test)
    # ImGuiItemStatusFlags_HasDisplayRect     = 1 << 1,       /* original C++ signature */
    has_display_rect = enum.auto()  # (= 1 << 1)  # g.LastItemData.DisplayRect is valid
    # ImGuiItemStatusFlags_Edited             = 1 << 2,       /* original C++ signature */
    edited = (
        enum.auto()
    )  # (= 1 << 2)  # Value exposed by item was edited in the current frame (should match the bool return value of most widgets)
    # ImGuiItemStatusFlags_ToggledSelection   = 1 << 3,       /* original C++ signature */
    toggled_selection = (
        enum.auto()
    )  # (= 1 << 3)  # Set when Selectable(), TreeNode() reports toggling a selection. We can't report "Selected", only state changes, in order to easily handle clipping with less issues.
    # ImGuiItemStatusFlags_ToggledOpen        = 1 << 4,       /* original C++ signature */
    toggled_open = (
        enum.auto()
    )  # (= 1 << 4)  # Set when TreeNode() reports toggling their open state.
    # ImGuiItemStatusFlags_HasDeactivated     = 1 << 5,       /* original C++ signature */
    has_deactivated = (
        enum.auto()
    )  # (= 1 << 5)  # Set if the widget/group is able to provide data for the ImGuiItemStatusFlags_Deactivated flag.
    # ImGuiItemStatusFlags_Deactivated        = 1 << 6,       /* original C++ signature */
    deactivated = (
        enum.auto()
    )  # (= 1 << 6)  # Only valid if ImGuiItemStatusFlags_HasDeactivated is set.
    # ImGuiItemStatusFlags_HoveredWindow      = 1 << 7,       /* original C++ signature */
    hovered_window = (
        enum.auto()
    )  # (= 1 << 7)  # Override the HoveredWindow test to allow cross-window hover testing.
    # ImGuiItemStatusFlags_FocusedByTabbing   = 1 << 8,       /* original C++ signature */
    focused_by_tabbing = (
        enum.auto()
    )  # (= 1 << 8)  # Set when the Focusable item just got focused by Tabbing (FIXME: to be removed soon)
    # ImGuiItemStatusFlags_Visible            = 1 << 9,       /* original C++ signature */
    visible = (
        enum.auto()
    )  # (= 1 << 9)  # [WIP] Set when item is overlapping the current clipping rectangle (Used internally. Please don't use yet: API/system will change as we refactor Itemadd()).

    # Additional status + semantic for ImGuiTestEngine

class HoveredFlagsPrivate_(enum.Enum):
    """Extend ImGuiHoveredFlags_"""

    # ImGuiHoveredFlags_DelayMask_                    = ImGuiHoveredFlags_DelayNone | ImGuiHoveredFlags_DelayShort | ImGuiHoveredFlags_DelayNormal | ImGuiHoveredFlags_NoSharedDelay,    /* original C++ signature */
    im_gui_hovered_flags_delay_mask_ = (
        enum.auto()
    )  # (= HoveredFlags_DelayNone | HoveredFlags_DelayShort | HoveredFlags_DelayNormal | HoveredFlags_NoSharedDelay)
    # ImGuiHoveredFlags_AllowedMaskForIsWindowHovered = ImGuiHoveredFlags_ChildWindows | ImGuiHoveredFlags_RootWindow | ImGuiHoveredFlags_AnyWindow | ImGuiHoveredFlags_NoPopupHierarchy | ImGuiHoveredFlags_DockHierarchy | ImGuiHoveredFlags_AllowWhenBlockedByPopup | ImGuiHoveredFlags_AllowWhenBlockedByActiveItem | ImGuiHoveredFlags_ForTooltip | ImGuiHoveredFlags_Stationary,    /* original C++ signature */
    im_gui_hovered_flags_allowed_mask_for_is_window_hovered = (
        enum.auto()
    )  # (= HoveredFlags_ChildWindows | HoveredFlags_RootWindow | HoveredFlags_AnyWindow | HoveredFlags_NoPopupHierarchy | HoveredFlags_DockHierarchy | HoveredFlags_AllowWhenBlockedByPopup | HoveredFlags_AllowWhenBlockedByActiveItem | HoveredFlags_ForTooltip | HoveredFlags_Stationary)
    # ImGuiHoveredFlags_AllowedMaskForIsItemHovered   = ImGuiHoveredFlags_AllowWhenBlockedByPopup | ImGuiHoveredFlags_AllowWhenBlockedByActiveItem | ImGuiHoveredFlags_AllowWhenOverlapped | ImGuiHoveredFlags_AllowWhenDisabled | ImGuiHoveredFlags_NoNavOverride | ImGuiHoveredFlags_ForTooltip | ImGuiHoveredFlags_Stationary | ImGuiHoveredFlags_DelayMask_,    /* original C++ signature */
    # }
    im_gui_hovered_flags_allowed_mask_for_is_item_hovered = (
        enum.auto()
    )  # (= HoveredFlags_AllowWhenBlockedByPopup | HoveredFlags_AllowWhenBlockedByActiveItem | HoveredFlags_AllowWhenOverlapped | HoveredFlags_AllowWhenDisabled | HoveredFlags_NoNavOverride | HoveredFlags_ForTooltip | HoveredFlags_Stationary | HoveredFlags_DelayMask_)

class InputTextFlagsPrivate_(enum.Enum):
    """Extend ImGuiInputTextFlags_"""

    # [Internal]
    # ImGuiInputTextFlags_Multiline           = 1 << 26,      /* original C++ signature */
    im_gui_input_text_flags_multiline = (
        enum.auto()
    )  # (= 1 << 26)  # For internal use by InputTextMultiline()
    # ImGuiInputTextFlags_NoMarkEdited        = 1 << 27,      /* original C++ signature */
    im_gui_input_text_flags_no_mark_edited = (
        enum.auto()
    )  # (= 1 << 27)  # For internal use by functions using InputText() before reformatting data
    # ImGuiInputTextFlags_MergedItem          = 1 << 28,      /* original C++ signature */
    im_gui_input_text_flags_merged_item = (
        enum.auto()
    )  # (= 1 << 28)  # For internal use by TempInputText(), will skip calling ItemAdd(). Require bounding-box to strictly match.

class ButtonFlagsPrivate_(enum.Enum):
    """Extend ImGuiButtonFlags_"""

    # ImGuiButtonFlags_PressedOnClick         = 1 << 4,       /* original C++ signature */
    im_gui_button_flags_pressed_on_click = (
        enum.auto()
    )  # (= 1 << 4)  # return True on click (mouse down event)
    # ImGuiButtonFlags_PressedOnClickRelease  = 1 << 5,       /* original C++ signature */
    im_gui_button_flags_pressed_on_click_release = (
        enum.auto()
    )  # (= 1 << 5)  # [Default] return True on click + release on same item <-- this is what the majority of Button are using
    # ImGuiButtonFlags_PressedOnClickReleaseAnywhere = 1 << 6,     /* original C++ signature */
    im_gui_button_flags_pressed_on_click_release_anywhere = (
        enum.auto()
    )  # (= 1 << 6)  # return True on click + release even if the release event is not done while hovering the item
    # ImGuiButtonFlags_PressedOnRelease       = 1 << 7,       /* original C++ signature */
    im_gui_button_flags_pressed_on_release = (
        enum.auto()
    )  # (= 1 << 7)  # return True on release (default requires click+release)
    # ImGuiButtonFlags_PressedOnDoubleClick   = 1 << 8,       /* original C++ signature */
    im_gui_button_flags_pressed_on_double_click = (
        enum.auto()
    )  # (= 1 << 8)  # return True on double-click (default requires click+release)
    # ImGuiButtonFlags_PressedOnDragDropHold  = 1 << 9,       /* original C++ signature */
    im_gui_button_flags_pressed_on_drag_drop_hold = (
        enum.auto()
    )  # (= 1 << 9)  # return True when held into while we are drag and dropping another item (used by e.g. tree nodes, collapsing headers)
    # ImGuiButtonFlags_Repeat                 = 1 << 10,      /* original C++ signature */
    im_gui_button_flags_repeat = enum.auto()  # (= 1 << 10)  # hold to repeat
    # ImGuiButtonFlags_FlattenChildren        = 1 << 11,      /* original C++ signature */
    im_gui_button_flags_flatten_children = (
        enum.auto()
    )  # (= 1 << 11)  # allow interactions even if a child window is overlapping
    # ImGuiButtonFlags_AllowOverlap           = 1 << 12,      /* original C++ signature */
    im_gui_button_flags_allow_overlap = (
        enum.auto()
    )  # (= 1 << 12)  # require previous frame HoveredId to either match id or be null before being usable.
    # ImGuiButtonFlags_DontClosePopups        = 1 << 13,      /* original C++ signature */
    im_gui_button_flags_dont_close_popups = (
        enum.auto()
    )  # (= 1 << 13)  # disable automatically closing parent popup on press // [UNUSED]
    # ImGuiButtonFlags_Disabled             = 1 << 14,  // disable interactions -> use BeginDisabled() or ImGuiItemFlags_Disabled
    # ImGuiButtonFlags_AlignTextBaseLine      = 1 << 15,      /* original C++ signature */
    im_gui_button_flags_align_text_base_line = (
        enum.auto()
    )  # (= 1 << 15)  # vertically align button to match text baseline - ButtonEx() only // FIXME: Should be removed and handled by SmallButton(), not possible currently because of DC.CursorPosPrevLine
    # ImGuiButtonFlags_NoKeyModifiers         = 1 << 16,      /* original C++ signature */
    im_gui_button_flags_no_key_modifiers = (
        enum.auto()
    )  # (= 1 << 16)  # disable mouse interaction if a key modifier is held
    # ImGuiButtonFlags_NoHoldingActiveId      = 1 << 17,      /* original C++ signature */
    im_gui_button_flags_no_holding_active_id = (
        enum.auto()
    )  # (= 1 << 17)  # don't set ActiveId while holding the mouse (ImGuiButtonFlags_PressedOnClick only)
    # ImGuiButtonFlags_NoNavFocus             = 1 << 18,      /* original C++ signature */
    im_gui_button_flags_no_nav_focus = (
        enum.auto()
    )  # (= 1 << 18)  # don't override navigation focus when activated (FIXME: this is essentially used everytime an item uses ImGuiItemFlags_NoNav, but because legacy specs don't requires LastItemData to be set ButtonBehavior(), we can't poll g.LastItemData.InFlags)
    # ImGuiButtonFlags_NoHoveredOnFocus       = 1 << 19,      /* original C++ signature */
    im_gui_button_flags_no_hovered_on_focus = (
        enum.auto()
    )  # (= 1 << 19)  # don't report as hovered when nav focus is on this item
    # ImGuiButtonFlags_NoSetKeyOwner          = 1 << 20,      /* original C++ signature */
    im_gui_button_flags_no_set_key_owner = (
        enum.auto()
    )  # (= 1 << 20)  # don't set key/input owner on the initial click (note: mouse buttons are keys! often, the key in question will be ImGuiKey_MouseLeft!)
    # ImGuiButtonFlags_NoTestKeyOwner         = 1 << 21,      /* original C++ signature */
    im_gui_button_flags_no_test_key_owner = (
        enum.auto()
    )  # (= 1 << 21)  # don't test key/input owner when polling the key (note: mouse buttons are keys! often, the key in question will be ImGuiKey_MouseLeft!)
    # ImGuiButtonFlags_PressedOnMask_         = ImGuiButtonFlags_PressedOnClick | ImGuiButtonFlags_PressedOnClickRelease | ImGuiButtonFlags_PressedOnClickReleaseAnywhere | ImGuiButtonFlags_PressedOnRelease | ImGuiButtonFlags_PressedOnDoubleClick | ImGuiButtonFlags_PressedOnDragDropHold,    /* original C++ signature */
    im_gui_button_flags_pressed_on_mask_ = (
        enum.auto()
    )  # (= ButtonFlags_PressedOnClick | ButtonFlags_PressedOnClickRelease | ButtonFlags_PressedOnClickReleaseAnywhere | ButtonFlags_PressedOnRelease | ButtonFlags_PressedOnDoubleClick | ButtonFlags_PressedOnDragDropHold)
    # ImGuiButtonFlags_PressedOnDefault_      = ImGuiButtonFlags_PressedOnClickRelease,    /* original C++ signature */
    # }
    im_gui_button_flags_pressed_on_default_ = (
        enum.auto()
    )  # (= ButtonFlags_PressedOnClickRelease)

class ComboFlagsPrivate_(enum.Enum):
    """Extend ImGuiComboFlags_"""

    # ImGuiComboFlags_CustomPreview           = 1 << 20,      /* original C++ signature */
    im_gui_combo_flags_custom_preview = (
        enum.auto()
    )  # (= 1 << 20)  # enable BeginComboPreview()

class SliderFlagsPrivate_(enum.Enum):
    """Extend ImGuiSliderFlags_"""

    # ImGuiSliderFlags_Vertical               = 1 << 20,      /* original C++ signature */
    im_gui_slider_flags_vertical = (
        enum.auto()
    )  # (= 1 << 20)  # Should this slider be orientated vertically?
    # ImGuiSliderFlags_ReadOnly               = 1 << 21,      /* original C++ signature */
    im_gui_slider_flags_read_only = (
        enum.auto()
    )  # (= 1 << 21)  # Consider using g.NextItemData.ItemFlags |= ImGuiItemFlags_ReadOnly instead.

class SelectableFlagsPrivate_(enum.Enum):
    """Extend ImGuiSelectableFlags_"""

    # NB: need to be in sync with last value of ImGuiSelectableFlags_
    # ImGuiSelectableFlags_NoHoldingActiveID      = 1 << 20,    /* original C++ signature */
    no_holding_active_id = enum.auto()  # (= 1 << 20)
    # ImGuiSelectableFlags_SelectOnNav            = 1 << 21,      /* original C++ signature */
    select_on_nav = (
        enum.auto()
    )  # (= 1 << 21)  # (WIP) Auto-select when moved into. This is not exposed in public API as to handle multi-select and modifiers we will need user to explicitly control focus scope. May be replaced with a BeginSelection() API.
    # ImGuiSelectableFlags_SelectOnClick          = 1 << 22,      /* original C++ signature */
    select_on_click = (
        enum.auto()
    )  # (= 1 << 22)  # Override button behavior to react on Click (default is Click+Release)
    # ImGuiSelectableFlags_SelectOnRelease        = 1 << 23,      /* original C++ signature */
    select_on_release = (
        enum.auto()
    )  # (= 1 << 23)  # Override button behavior to react on Release (default is Click+Release)
    # ImGuiSelectableFlags_SpanAvailWidth         = 1 << 24,      /* original C++ signature */
    span_avail_width = (
        enum.auto()
    )  # (= 1 << 24)  # Span all avail width even if we declared less for layout purpose. FIXME: We may be able to remove this (added in 6251379, 2bcafc86 for menus)
    # ImGuiSelectableFlags_SetNavIdOnHover        = 1 << 25,      /* original C++ signature */
    set_nav_id_on_hover = (
        enum.auto()
    )  # (= 1 << 25)  # Set Nav/Focus ID on mouse hover (used by MenuItem)
    # ImGuiSelectableFlags_NoPadWithHalfSpacing   = 1 << 26,      /* original C++ signature */
    no_pad_with_half_spacing = (
        enum.auto()
    )  # (= 1 << 26)  # Disable padding each side with ItemSpacing * 0.5
    # ImGuiSelectableFlags_NoSetKeyOwner          = 1 << 27,      /* original C++ signature */
    no_set_key_owner = (
        enum.auto()
    )  # (= 1 << 27)  # Don't set key/input owner on the initial click (note: mouse buttons are keys! often, the key in question will be ImGuiKey_MouseLeft!)

class TreeNodeFlagsPrivate_(enum.Enum):
    """Extend ImGuiTreeNodeFlags_"""

    # ImGuiTreeNodeFlags_ClipLabelForTrailingButton = 1 << 20,    /* original C++ signature */
    im_gui_tree_node_flags_clip_label_for_trailing_button = enum.auto()  # (= 1 << 20)
    # ImGuiTreeNodeFlags_UpsideDownArrow            = 1 << 21,    /* original C++ signature */
    im_gui_tree_node_flags_upside_down_arrow = (
        enum.auto()
    )  # (= 1 << 21)  # (FIXME-WIP) Turn Down arrow into an Up arrow, but reversed trees (#6517)

class SeparatorFlags_(enum.Enum):
    # ImGuiSeparatorFlags_None                    = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiSeparatorFlags_Horizontal              = 1 << 0,       /* original C++ signature */
    horizontal = (
        enum.auto()
    )  # (= 1 << 0)  # Axis default to current layout type, so generally Horizontal unless e.g. in a menu bar
    # ImGuiSeparatorFlags_Vertical                = 1 << 1,    /* original C++ signature */
    vertical = enum.auto()  # (= 1 << 1)
    # ImGuiSeparatorFlags_SpanAllColumns          = 1 << 2,       /* original C++ signature */
    span_all_columns = (
        enum.auto()
    )  # (= 1 << 2)  # Make separator cover all columns of a legacy Columns() set.

class FocusRequestFlags_(enum.Enum):
    """Flags for FocusWindow(). This is not called ImGuiFocusFlags to avoid confusion with public-facing ImGuiFocusedFlags.
    FIXME: Once we finishing replacing more uses of GetTopMostPopupModal()+IsWindowWithinBeginStackOf()
    and FindBlockingModal() with this, we may want to change the flag to be opt-out instead of opt-in.
    """

    # ImGuiFocusRequestFlags_None                 = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiFocusRequestFlags_RestoreFocusedChild  = 1 << 0,       /* original C++ signature */
    restore_focused_child = (
        enum.auto()
    )  # (= 1 << 0)  # Find last focused child (if any) and focus it instead.
    # ImGuiFocusRequestFlags_UnlessBelowModal     = 1 << 1,       /* original C++ signature */
    unless_below_modal = (
        enum.auto()
    )  # (= 1 << 1)  # Do not set focus if the window is below a modal.

class TextFlags_(enum.Enum):
    # ImGuiTextFlags_None                         = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiTextFlags_NoWidthForLargeClippedText   = 1 << 0,    /* original C++ signature */
    # }
    no_width_for_large_clipped_text = enum.auto()  # (= 1 << 0)

class TooltipFlags_(enum.Enum):
    # ImGuiTooltipFlags_None                      = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiTooltipFlags_OverridePrevious          = 1 << 1,       /* original C++ signature */
    override_previous = (
        enum.auto()
    )  # (= 1 << 1)  # Clear/ignore previously submitted tooltip (defaults to append)

class LayoutType_(enum.Enum):
    """FIXME: this is in development, not exposed/functional as a generic feature yet.
    Horizontal/Vertical enums are fixed to 0/1 so they may be used to index ImVec2
    """

    # ImGuiLayoutType_Horizontal = 0,    /* original C++ signature */
    horizontal = enum.auto()  # (= 0)
    # ImGuiLayoutType_Vertical = 1    /* original C++ signature */
    # }
    vertical = enum.auto()  # (= 1)

class LogType(enum.Enum):
    # ImGuiLogType_None = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiLogType_TTY,    /* original C++ signature */
    tty = enum.auto()  # (= 1)
    # ImGuiLogType_File,    /* original C++ signature */
    file = enum.auto()  # (= 2)
    # ImGuiLogType_Buffer,    /* original C++ signature */
    buffer = enum.auto()  # (= 3)
    # ImGuiLogType_Clipboard,    /* original C++ signature */
    # }
    clipboard = enum.auto()  # (= 4)

class Axis(enum.Enum):
    """X/Y enums are fixed to 0/1 so they may be used to index ImVec2"""

    # ImGuiAxis_None = -1,    /* original C++ signature */
    none = enum.auto()  # (= -1)
    # ImGuiAxis_X = 0,    /* original C++ signature */
    x = enum.auto()  # (= 0)
    # ImGuiAxis_Y = 1    /* original C++ signature */
    # }
    y = enum.auto()  # (= 1)

class PlotType(enum.Enum):
    # ImGuiPlotType_Lines,    /* original C++ signature */
    lines = enum.auto()  # (= 0)
    # ImGuiPlotType_Histogram,    /* original C++ signature */
    # }
    histogram = enum.auto()  # (= 1)

class PopupPositionPolicy(enum.Enum):
    # ImGuiPopupPositionPolicy_Default,    /* original C++ signature */
    default = enum.auto()  # (= 0)
    # ImGuiPopupPositionPolicy_ComboBox,    /* original C++ signature */
    combo_box = enum.auto()  # (= 1)
    # ImGuiPopupPositionPolicy_Tooltip,    /* original C++ signature */
    # }
    tooltip = enum.auto()  # (= 2)

class DataVarInfo:
    # ImGuiDataType   Type;    /* original C++ signature */
    type: DataType
    # ImU32           Count;    /* original C++ signature */
    count: ImU32  # 1+
    # ImU32           Offset;    /* original C++ signature */
    offset: ImU32  # Offset in parent structure
    # void* GetVarPtr(void* parent) const { return (void*)((uchar*)parent + Offset); }    /* original C++ signature */
    def get_var_ptr(self, parent: Any) -> Any:
        """(private API)"""
        pass
    # ImGuiDataVarInfo(ImGuiDataType Type = ImGuiDataType(), ImU32 Count = ImU32(), ImU32 Offset = ImU32());    /* original C++ signature */
    def __init__(
        self,
        type: DataType = DataType(),
        count: ImU32 = ImU32(),
        offset: ImU32 = ImU32(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class DataTypeTempStorage:
    # ImU8        Data[8];    /* original C++ signature */
    data: np.ndarray  # ndarray[type=ImU8, size=8]  # Can fit any data up to ImGuiDataType_COUNT
    # ImGuiDataTypeTempStorage();    /* original C++ signature */
    def __init__(self) -> None:
        """Auto-generated default constructor"""
        pass

class DataTypeInfo:
    """Type information associated to one ImGuiDataType. Retrieve with DataTypeGetInfo()."""

    # size_t      Size;    /* original C++ signature */
    size: int  # Size in bytes
    # const char* Name;    /* original C++ signature */
    name: str  # Short descriptive name for the type, for debugging # (const)
    # const char* PrintFmt;    /* original C++ signature */
    print_fmt: str  # Default printf format for the type # (const)
    # const char* ScanFmt;    /* original C++ signature */
    scan_fmt: str  # Default scanf format for the type # (const)
    # ImGuiDataTypeInfo(size_t Size = size_t());    /* original C++ signature */
    def __init__(self, size: int = int()) -> None:
        """Auto-generated default constructor with named params"""
        pass

class DataTypePrivate_(enum.Enum):
    """Extend ImGuiDataType_"""

    # ImGuiDataType_String = ImGuiDataType_COUNT + 1,    /* original C++ signature */
    im_gui_data_type_string = enum.auto()  # (= DataType_COUNT + 1)
    # ImGuiDataType_Pointer,    /* original C++ signature */
    im_gui_data_type_pointer = enum.auto()  # (= )
    # ImGuiDataType_ID,    /* original C++ signature */
    # }
    im_gui_data_type_id = enum.auto()  # (= )

class ColorMod:
    """Stacked color modifier, backup of modified data so we can restore it"""

    # ImGuiCol        Col;    /* original C++ signature */
    col: Col
    # ImVec4          BackupValue;    /* original C++ signature */
    backup_value: ImVec4
    # ImGuiColorMod(ImGuiCol Col = ImGuiCol(), ImVec4 BackupValue = ImVec4());    /* original C++ signature */
    def __init__(self, col: Col = Col(), backup_value: ImVec4 = ImVec4()) -> None:
        """Auto-generated default constructor with named params"""
        pass

class StyleMod:
    """Stacked style modifier, backup of modified data so we can restore it. Data type inferred from the variable."""

    # ImGuiStyleVar   VarIdx;    /* original C++ signature */
    var_idx: StyleVar
    # ImGuiStyleMod(ImGuiStyleVar idx, int v)     { VarIdx = idx; BackupInt[0] = v; }    /* original C++ signature */
    @overload
    def __init__(self, idx: StyleVar, v: int) -> None:
        pass
    # ImGuiStyleMod(ImGuiStyleVar idx, float v)   { VarIdx = idx; BackupFloat[0] = v; }    /* original C++ signature */
    @overload
    def __init__(self, idx: StyleVar, v: float) -> None:
        pass
    # ImGuiStyleMod(ImGuiStyleVar idx, ImVec2 v)  { VarIdx = idx; BackupFloat[0] = v.x; BackupFloat[1] = v.y; }    /* original C++ signature */
    @overload
    def __init__(self, idx: StyleVar, v: ImVec2) -> None:
        pass

class ComboPreviewData:
    """Storage data for BeginComboPreview()/EndComboPreview()"""

    # ImRect          PreviewRect;    /* original C++ signature */
    preview_rect: ImRect
    # ImVec2          BackupCursorPos;    /* original C++ signature */
    backup_cursor_pos: ImVec2
    # ImVec2          BackupCursorMaxPos;    /* original C++ signature */
    backup_cursor_max_pos: ImVec2
    # ImVec2          BackupCursorPosPrevLine;    /* original C++ signature */
    backup_cursor_pos_prev_line: ImVec2
    # float           BackupPrevLineTextBaseOffset;    /* original C++ signature */
    backup_prev_line_text_base_offset: float
    # ImGuiLayoutType BackupLayout;    /* original C++ signature */
    backup_layout: LayoutType

    # ImGuiComboPreviewData() { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class GroupData:
    """Stacked storage data for BeginGroup()/EndGroup()"""

    # ImGuiID     WindowID;    /* original C++ signature */
    window_id: ID
    # ImVec2      BackupCursorPos;    /* original C++ signature */
    backup_cursor_pos: ImVec2
    # ImVec2      BackupCursorMaxPos;    /* original C++ signature */
    backup_cursor_max_pos: ImVec2
    # ImVec2      BackupCursorPosPrevLine;    /* original C++ signature */
    backup_cursor_pos_prev_line: ImVec2
    # ImVec1      BackupIndent;    /* original C++ signature */
    backup_indent: ImVec1
    # ImVec1      BackupGroupOffset;    /* original C++ signature */
    backup_group_offset: ImVec1
    # ImVec2      BackupCurrLineSize;    /* original C++ signature */
    backup_curr_line_size: ImVec2
    # float       BackupCurrLineTextBaseOffset;    /* original C++ signature */
    backup_curr_line_text_base_offset: float
    # ImGuiID     BackupActiveIdIsAlive;    /* original C++ signature */
    backup_active_id_is_alive: ID
    # bool        BackupActiveIdPreviousFrameIsAlive;    /* original C++ signature */
    backup_active_id_previous_frame_is_alive: bool
    # bool        BackupHoveredIdIsAlive;    /* original C++ signature */
    backup_hovered_id_is_alive: bool
    # bool        BackupIsSameLine;    /* original C++ signature */
    backup_is_same_line: bool
    # bool        EmitItem;    /* original C++ signature */
    emit_item: bool
    # ImGuiGroupData(ImGuiID WindowID = ImGuiID(), ImVec2 BackupCursorPos = ImVec2(), ImVec2 BackupCursorMaxPos = ImVec2(), ImVec2 BackupCursorPosPrevLine = ImVec2(), ImVec1 BackupIndent = ImVec1(), ImVec1 BackupGroupOffset = ImVec1(), ImVec2 BackupCurrLineSize = ImVec2(), float BackupCurrLineTextBaseOffset = float(), ImGuiID BackupActiveIdIsAlive = ImGuiID(), bool BackupActiveIdPreviousFrameIsAlive = bool(), bool BackupHoveredIdIsAlive = bool(), bool BackupIsSameLine = bool(), bool EmitItem = bool());    /* original C++ signature */
    def __init__(
        self,
        window_id: ID = ID(),
        backup_cursor_pos: ImVec2 = ImVec2(),
        backup_cursor_max_pos: ImVec2 = ImVec2(),
        backup_cursor_pos_prev_line: ImVec2 = ImVec2(),
        backup_indent: ImVec1 = ImVec1(),
        backup_group_offset: ImVec1 = ImVec1(),
        backup_curr_line_size: ImVec2 = ImVec2(),
        backup_curr_line_text_base_offset: float = float(),
        backup_active_id_is_alive: ID = ID(),
        backup_active_id_previous_frame_is_alive: bool = bool(),
        backup_hovered_id_is_alive: bool = bool(),
        backup_is_same_line: bool = bool(),
        emit_item: bool = bool(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class MenuColumns:
    """Simple column measurement, currently used for MenuItem() only.. This is very short-sighted/throw-away code and NOT a generic helper."""

    # ImU32       TotalWidth;    /* original C++ signature */
    total_width: ImU32
    # ImU32       NextTotalWidth;    /* original C++ signature */
    next_total_width: ImU32
    # ImU16       Spacing;    /* original C++ signature */
    spacing: ImU16
    # ImU16       OffsetIcon;    /* original C++ signature */
    offset_icon: ImU16  # Always zero for now
    # ImU16       OffsetLabel;    /* original C++ signature */
    offset_label: ImU16  # Offsets are locked in Update()
    # ImU16       OffsetShortcut;    /* original C++ signature */
    offset_shortcut: ImU16
    # ImU16       OffsetMark;    /* original C++ signature */
    offset_mark: ImU16
    # ImU16       Widths[4];    /* original C++ signature */
    widths: np.ndarray  # ndarray[type=ImU16, size=4]  # Width of:   Icon, Label, Shortcut, Mark  (accumulators for current frame)

    # ImGuiMenuColumns() { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # void        Update(float spacing, bool window_reappearing);    /* original C++ signature */
    def update(self, spacing: float, window_reappearing: bool) -> None:
        """(private API)"""
        pass
    # float       DeclColumns(float w_icon, float w_label, float w_shortcut, float w_mark);    /* original C++ signature */
    def decl_columns(
        self, w_icon: float, w_label: float, w_shortcut: float, w_mark: float
    ) -> float:
        """(private API)"""
        pass
    # void        CalcNextTotalWidth(bool update_offsets);    /* original C++ signature */
    def calc_next_total_width(self, update_offsets: bool) -> None:
        """(private API)"""
        pass

class InputTextDeactivatedState:
    """Internal temporary state for deactivating InputText() instances."""

    # ImGuiID            ID;    /* original C++ signature */
    id_: ID  # widget id owning the text state (which just got deactivated)
    # ImVector<char>     TextA;    /* original C++ signature */
    text_a: ImVector_char  # text buffer

    # ImGuiInputTextDeactivatedState()    { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # void    ClearFreeMemory()           { ID = 0; TextA.clear(); }    /* original C++ signature */
    def clear_free_memory(self) -> None:
        """(private API)"""
        pass

class InputTextState:
    """Internal state of the currently focused/edited text input box
    For a given item ID, access with ImGui::GetInputTextState()
    """

    # ImGuiContext*           Ctx;    /* original C++ signature */
    ctx: Context  # parent UI context (needs to be set explicitly by parent).
    # ImGuiID                 ID;    /* original C++ signature */
    id_: ID  # widget id owning the text state
    # int                     CurLenW,     /* original C++ signature */
    cur_len_w: int  # we need to maintain our buffer length in both UTF-8 and wchar format. UTF-8 length is valid even if TextA is not.
    # CurLenA;    /* original C++ signature */
    cur_len_a: int  # we need to maintain our buffer length in both UTF-8 and wchar format. UTF-8 length is valid even if TextA is not.
    # ImVector<ImWchar>       TextW;    /* original C++ signature */
    text_w: ImVector_ImWchar  # edit buffer, we need to persist but can't guarantee the persistence of the user-provided buffer. so we copy into own buffer.
    # ImVector<char>          TextA;    /* original C++ signature */
    text_a: ImVector_char  # temporary UTF8 buffer for callbacks and other operations. this is not updated in every code-path! size=capacity.
    # ImVector<char>          InitialTextA;    /* original C++ signature */
    initial_text_a: ImVector_char  # backup of end-user buffer at the time of focus (in UTF-8, unaltered)
    # bool                    TextAIsValid;    /* original C++ signature */
    text_a_is_valid: bool  # temporary UTF8 buffer is not initially valid before we make the widget active (until then we pull the data from user argument)
    # int                     BufCapacityA;    /* original C++ signature */
    buf_capacity_a: int  # end-user buffer capacity
    # float                   ScrollX;    /* original C++ signature */
    scroll_x: float  # horizontal scrolling/offset
    # float                   CursorAnim;    /* original C++ signature */
    cursor_anim: float  # timer for cursor blink, reset on every user action so the cursor reappears immediately
    # bool                    CursorFollow;    /* original C++ signature */
    cursor_follow: bool  # set when we want scrolling to follow the current cursor position (not always!)
    # bool                    SelectedAllMouseLock;    /* original C++ signature */
    selected_all_mouse_lock: bool  # after a double-click to select all, we ignore further mouse drags to update selection
    # bool                    Edited;    /* original C++ signature */
    edited: bool  # edited this frame
    # ImGuiInputTextFlags     Flags;    /* original C++ signature */
    flags: InputTextFlags  # copy of InputText() flags. may be used to check if e.g. ImGuiInputTextFlags_Password is set.

    # ImGuiInputTextState()                   { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # void        ClearText()                 { CurLenW = CurLenA = 0; TextW[0] = 0; TextA[0] = 0; CursorClamp(); }    /* original C++ signature */
    def clear_text(self) -> None:
        """(private API)"""
        pass
    # void        ClearFreeMemory()           { TextW.clear(); TextA.clear(); InitialTextA.clear(); }    /* original C++ signature */
    def clear_free_memory(self) -> None:
        """(private API)"""
        pass
    # int         GetUndoAvailCount() const   { return Stb.undostate.undo_point; }    /* original C++ signature */
    def get_undo_avail_count(self) -> int:
        """(private API)"""
        pass
    # int         GetRedoAvailCount() const   { return STB_TEXTEDIT_UNDOSTATECOUNT - Stb.undostate.redo_point; }    /* original C++ signature */
    def get_redo_avail_count(self) -> int:
        """(private API)"""
        pass
    # void        OnKeyPressed(int key);          /* original C++ signature */
    def on_key_pressed(self, key: int) -> None:
        """(private API)

        Cannot be inline because we call in code in stb_textedit.h implementation
        """
        pass
    # Cursor & Selection
    # void        CursorAnimReset()           { CursorAnim = -0.30f; }                                       /* original C++ signature */
    def cursor_anim_reset(self) -> None:
        """(private API)

        After a user-input the cursor stays on for a while without blinking
        """
        pass
    # void        CursorClamp()               { Stb.cursor = ImMin(Stb.cursor, CurLenW); Stb.select_start = ImMin(Stb.select_start, CurLenW); Stb.select_end = ImMin(Stb.select_end, CurLenW); }    /* original C++ signature */
    def cursor_clamp(self) -> None:
        """(private API)"""
        pass
    # bool        HasSelection() const        { return Stb.select_start != Stb.select_end; }    /* original C++ signature */
    def has_selection(self) -> bool:
        """(private API)"""
        pass
    # void        ClearSelection()            { Stb.select_start = Stb.select_end = Stb.cursor; }    /* original C++ signature */
    def clear_selection(self) -> None:
        """(private API)"""
        pass
    # int         GetCursorPos() const        { return Stb.cursor; }    /* original C++ signature */
    def get_cursor_pos(self) -> int:
        """(private API)"""
        pass
    # int         GetSelectionStart() const   { return Stb.select_start; }    /* original C++ signature */
    def get_selection_start(self) -> int:
        """(private API)"""
        pass
    # int         GetSelectionEnd() const     { return Stb.select_end; }    /* original C++ signature */
    def get_selection_end(self) -> int:
        """(private API)"""
        pass
    # void        SelectAll()                 { Stb.select_start = 0; Stb.cursor = Stb.select_end = CurLenW; Stb.has_preferred_x = 0; }    /* original C++ signature */
    def select_all(self) -> None:
        """(private API)"""
        pass

class PopupData:
    """Storage for current popup stack"""

    # ImGuiID             PopupId;    /* original C++ signature */
    popup_id: ID  # Set on OpenPopup()
    # ImGuiWindow*        Window;    /* original C++ signature */
    window: Window  # Resolved on BeginPopup() - may stay unresolved if user never calls OpenPopup()
    # ImGuiWindow*        BackupNavWindow;    /* original C++ signature */
    backup_nav_window: Window  # Set on OpenPopup(), a NavWindow that will be restored on popup close
    # int                 ParentNavLayer;    /* original C++ signature */
    parent_nav_layer: int  # Resolved on BeginPopup(). Actually a ImGuiNavLayer type (declared down below), initialized to -1 which is not part of an enum, but serves well-enough as "not any of layers" value
    # int                 OpenFrameCount;    /* original C++ signature */
    open_frame_count: int  # Set on OpenPopup()
    # ImGuiID             OpenParentId;    /* original C++ signature */
    open_parent_id: ID  # Set on OpenPopup(), we need this to differentiate multiple menu sets from each others (e.g. inside menu bar vs loose menu items)
    # ImVec2              OpenPopupPos;    /* original C++ signature */
    open_popup_pos: ImVec2  # Set on OpenPopup(), preferred popup position (typically == OpenMousePos when using mouse)
    # ImVec2              OpenMousePos;    /* original C++ signature */
    open_mouse_pos: ImVec2  # Set on OpenPopup(), copy of mouse position at the time of opening popup

    # ImGuiPopupData()    { memset(this, 0, sizeof(*this)); ParentNavLayer = OpenFrameCount = -1; }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class NextWindowDataFlags_(enum.Enum):
    # ImGuiNextWindowDataFlags_None               = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiNextWindowDataFlags_HasPos             = 1 << 0,    /* original C++ signature */
    has_pos = enum.auto()  # (= 1 << 0)
    # ImGuiNextWindowDataFlags_HasSize            = 1 << 1,    /* original C++ signature */
    has_size = enum.auto()  # (= 1 << 1)
    # ImGuiNextWindowDataFlags_HasContentSize     = 1 << 2,    /* original C++ signature */
    has_content_size = enum.auto()  # (= 1 << 2)
    # ImGuiNextWindowDataFlags_HasCollapsed       = 1 << 3,    /* original C++ signature */
    has_collapsed = enum.auto()  # (= 1 << 3)
    # ImGuiNextWindowDataFlags_HasSizeConstraint  = 1 << 4,    /* original C++ signature */
    has_size_constraint = enum.auto()  # (= 1 << 4)
    # ImGuiNextWindowDataFlags_HasFocus           = 1 << 5,    /* original C++ signature */
    has_focus = enum.auto()  # (= 1 << 5)
    # ImGuiNextWindowDataFlags_HasBgAlpha         = 1 << 6,    /* original C++ signature */
    has_bg_alpha = enum.auto()  # (= 1 << 6)
    # ImGuiNextWindowDataFlags_HasScroll          = 1 << 7,    /* original C++ signature */
    has_scroll = enum.auto()  # (= 1 << 7)
    # ImGuiNextWindowDataFlags_HasChildFlags      = 1 << 8,    /* original C++ signature */
    has_child_flags = enum.auto()  # (= 1 << 8)
    # ImGuiNextWindowDataFlags_HasViewport        = 1 << 9,    /* original C++ signature */
    has_viewport = enum.auto()  # (= 1 << 9)
    # ImGuiNextWindowDataFlags_HasDock            = 1 << 10,    /* original C++ signature */
    has_dock = enum.auto()  # (= 1 << 10)
    # ImGuiNextWindowDataFlags_HasWindowClass     = 1 << 11,    /* original C++ signature */
    # }
    has_window_class = enum.auto()  # (= 1 << 11)

class NextWindowData:
    """Storage for SetNexWindow** functions"""

    # ImGuiNextWindowDataFlags    Flags;    /* original C++ signature */
    flags: NextWindowDataFlags
    # ImGuiCond                   PosCond;    /* original C++ signature */
    pos_cond: Cond
    # ImGuiCond                   SizeCond;    /* original C++ signature */
    size_cond: Cond
    # ImGuiCond                   CollapsedCond;    /* original C++ signature */
    collapsed_cond: Cond
    # ImGuiCond                   DockCond;    /* original C++ signature */
    dock_cond: Cond
    # ImVec2                      PosVal;    /* original C++ signature */
    pos_val: ImVec2
    # ImVec2                      PosPivotVal;    /* original C++ signature */
    pos_pivot_val: ImVec2
    # ImVec2                      SizeVal;    /* original C++ signature */
    size_val: ImVec2
    # ImVec2                      ContentSizeVal;    /* original C++ signature */
    content_size_val: ImVec2
    # ImVec2                      ScrollVal;    /* original C++ signature */
    scroll_val: ImVec2
    # ImGuiChildFlags             ChildFlags;    /* original C++ signature */
    child_flags: ChildFlags
    # bool                        PosUndock;    /* original C++ signature */
    pos_undock: bool
    # bool                        CollapsedVal;    /* original C++ signature */
    collapsed_val: bool
    # ImRect                      SizeConstraintRect;    /* original C++ signature */
    size_constraint_rect: ImRect
    # ImGuiSizeCallback           SizeCallback;    /* original C++ signature */
    size_callback: SizeCallback
    # void*                       SizeCallbackUserData;    /* original C++ signature */
    size_callback_user_data: Any
    # float                       BgAlphaVal;    /* original C++ signature */
    bg_alpha_val: float  # Override background alpha
    # ImGuiID                     ViewportId;    /* original C++ signature */
    viewport_id: ID
    # ImGuiID                     DockId;    /* original C++ signature */
    dock_id: ID
    # ImGuiWindowClass            WindowClass;    /* original C++ signature */
    window_class: WindowClass
    # ImVec2                      MenuBarOffsetMinVal;    /* original C++ signature */
    menu_bar_offset_min_val: ImVec2  # (Always on) This is not exposed publicly, so we don't clear it and it doesn't have a corresponding flag (could we? for consistency?)

    # ImGuiNextWindowData()       { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # inline void ClearFlags()    { Flags = ImGuiNextWindowDataFlags_None; }    /* original C++ signature */
    def clear_flags(self) -> None:
        """(private API)"""
        pass

class NextItemDataFlags_(enum.Enum):
    # ImGuiNextItemDataFlags_None     = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiNextItemDataFlags_HasWidth = 1 << 0,    /* original C++ signature */
    has_width = enum.auto()  # (= 1 << 0)
    # ImGuiNextItemDataFlags_HasOpen  = 1 << 1,    /* original C++ signature */
    # }
    has_open = enum.auto()  # (= 1 << 1)

class NextItemData:
    # ImGuiNextItemDataFlags      Flags;    /* original C++ signature */
    flags: NextItemDataFlags
    # ImGuiItemFlags              ItemFlags;    /* original C++ signature */
    item_flags: ItemFlags  # Currently only tested/used for ImGuiItemFlags_AllowOverlap.
    # Non-flags members are NOT cleared by ItemAdd() meaning they are still valid during NavProcessItem()
    # float                       Width;    /* original C++ signature */
    width: float  # Set by SetNextItemWidth()
    # ImGuiSelectionUserData      SelectionUserData;    /* original C++ signature */
    selection_user_data: SelectionUserData  # Set by SetNextItemSelectionUserData() (note that None/0 is a valid value, we use -1 == ImGuiSelectionUserData_Invalid to mark invalid values)
    # ImGuiCond                   OpenCond;    /* original C++ signature */
    open_cond: Cond
    # bool                        OpenVal;    /* original C++ signature */
    open_val: bool  # Set by SetNextItemOpen()

    # ImGuiNextItemData()         { memset(this, 0, sizeof(*this)); SelectionUserData = -1; }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # inline void ClearFlags()    { Flags = ImGuiNextItemDataFlags_None; ItemFlags = ImGuiItemFlags_None; }     /* original C++ signature */
    def clear_flags(self) -> None:
        """(private API)

        Also cleared manually by ItemAdd()!
        """
        pass

class LastItemData:
    """Status storage for the last submitted item"""

    # ImGuiID                 ID;    /* original C++ signature */
    id_: ID
    # ImGuiItemFlags          InFlags;    /* original C++ signature */
    in_flags: ItemFlags  # See ImGuiItemFlags_
    # ImGuiItemStatusFlags    StatusFlags;    /* original C++ signature */
    status_flags: ItemStatusFlags  # See ImGuiItemStatusFlags_
    # ImRect                  Rect;    /* original C++ signature */
    rect: ImRect  # Full rectangle
    # ImRect                  NavRect;    /* original C++ signature */
    nav_rect: ImRect  # Navigation scoring rectangle (not displayed)
    # ImRect                  DisplayRect;    /* original C++ signature */
    display_rect: ImRect  # Display rectangle (only if ImGuiItemStatusFlags_HasDisplayRect is set)

    # ImGuiLastItemData()     { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class NavTreeNodeData:
    """Store data emitted by TreeNode() for usage by TreePop() to implement ImGuiTreeNodeFlags_NavLeftJumpsBackHere.
    This is the minimum amount of data that we need to perform the equivalent of NavApplyItemToResult() and which we can't infer in TreePop()
    Only stored when the node is a potential candidate for landing on a Left arrow jump.
    """

    # ImGuiID                 ID;    /* original C++ signature */
    id_: ID
    # ImGuiItemFlags          InFlags;    /* original C++ signature */
    in_flags: ItemFlags
    # ImRect                  NavRect;    /* original C++ signature */
    nav_rect: ImRect
    # ImGuiNavTreeNodeData(ImGuiID ID = ImGuiID(), ImGuiItemFlags InFlags = ImGuiItemFlags(), ImRect NavRect = ImRect());    /* original C++ signature */
    def __init__(
        self,
        id_: ID = ID(),
        in_flags: ItemFlags = ItemFlags(),
        nav_rect: ImRect = ImRect(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class StackSizes:
    # short   SizeOfIDStack;    /* original C++ signature */
    size_of_id_stack: int
    # short   SizeOfColorStack;    /* original C++ signature */
    size_of_color_stack: int
    # short   SizeOfStyleVarStack;    /* original C++ signature */
    size_of_style_var_stack: int
    # short   SizeOfFontStack;    /* original C++ signature */
    size_of_font_stack: int
    # short   SizeOfFocusScopeStack;    /* original C++ signature */
    size_of_focus_scope_stack: int
    # short   SizeOfGroupStack;    /* original C++ signature */
    size_of_group_stack: int
    # short   SizeOfItemFlagsStack;    /* original C++ signature */
    size_of_item_flags_stack: int
    # short   SizeOfBeginPopupStack;    /* original C++ signature */
    size_of_begin_popup_stack: int
    # short   SizeOfDisabledStack;    /* original C++ signature */
    size_of_disabled_stack: int

    # ImGuiStackSizes() { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # void SetToContextState(ImGuiContext* ctx);    /* original C++ signature */
    def set_to_context_state(self, ctx: Context) -> None:
        """(private API)"""
        pass
    # void CompareWithContextState(ImGuiContext* ctx);    /* original C++ signature */
    def compare_with_context_state(self, ctx: Context) -> None:
        """(private API)"""
        pass

class WindowStackData:
    """Data saved for each window pushed into the stack"""

    # ImGuiWindow*        Window;    /* original C++ signature */
    window: Window
    # ImGuiLastItemData   ParentLastItemDataBackup;    /* original C++ signature */
    parent_last_item_data_backup: LastItemData
    # ImGuiStackSizes     StackSizesOnBegin;    /* original C++ signature */
    stack_sizes_on_begin: StackSizes  # Store size of various stacks for asserting
    # ImGuiWindowStackData(ImGuiLastItemData ParentLastItemDataBackup = ImGuiLastItemData(), ImGuiStackSizes StackSizesOnBegin = ImGuiStackSizes());    /* original C++ signature */
    def __init__(
        self,
        parent_last_item_data_backup: LastItemData = LastItemData(),
        stack_sizes_on_begin: StackSizes = StackSizes(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class ShrinkWidthItem:
    # int         Index;    /* original C++ signature */
    index: int
    # float       Width;    /* original C++ signature */
    width: float
    # float       InitialWidth;    /* original C++ signature */
    initial_width: float
    # ImGuiShrinkWidthItem(int Index = int(), float Width = float(), float InitialWidth = float());    /* original C++ signature */
    def __init__(
        self, index: int = int(), width: float = float(), initial_width: float = float()
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class PtrOrIndex:
    # void*       Ptr;    /* original C++ signature */
    ptr: Any  # Either field can be set, not both. e.g. Dock node tab bars are loose while BeginTabBar() ones are in a pool.
    # int         Index;    /* original C++ signature */
    index: int  # Usually index in a main pool.

    # ImGuiPtrOrIndex(void* ptr)  { Ptr = ptr; Index = -1; }    /* original C++ signature */
    @overload
    def __init__(self, ptr: Any) -> None:
        pass
    # ImGuiPtrOrIndex(int index)  { Ptr = NULL; Index = index; }    /* original C++ signature */
    @overload
    def __init__(self, index: int) -> None:
        pass

# -----------------------------------------------------------------------------
# [SECTION] Inputs support
# -----------------------------------------------------------------------------

# [Internal] Key ranges

# [Internal] Named shortcuts for Navigation

class InputEventType(enum.Enum):
    # ImGuiInputEventType_None = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiInputEventType_MousePos,    /* original C++ signature */
    mouse_pos = enum.auto()  # (= 1)
    # ImGuiInputEventType_MouseWheel,    /* original C++ signature */
    mouse_wheel = enum.auto()  # (= 2)
    # ImGuiInputEventType_MouseButton,    /* original C++ signature */
    mouse_button = enum.auto()  # (= 3)
    # ImGuiInputEventType_MouseViewport,    /* original C++ signature */
    mouse_viewport = enum.auto()  # (= 4)
    # ImGuiInputEventType_Key,    /* original C++ signature */
    key = enum.auto()  # (= 5)
    # ImGuiInputEventType_Text,    /* original C++ signature */
    text = enum.auto()  # (= 6)
    # ImGuiInputEventType_Focus,    /* original C++ signature */
    focus = enum.auto()  # (= 7)
    # ImGuiInputEventType_COUNT    /* original C++ signature */
    # }
    count = enum.auto()  # (= 8)

class InputSource(enum.Enum):
    # ImGuiInputSource_None = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiInputSource_Mouse,             /* original C++ signature */
    mouse = (
        enum.auto()
    )  # (= 1)  # Note: may be Mouse or TouchScreen or Pen. See io.MouseSource to distinguish them.
    # ImGuiInputSource_Keyboard,    /* original C++ signature */
    keyboard = enum.auto()  # (= 2)
    # ImGuiInputSource_Gamepad,    /* original C++ signature */
    gamepad = enum.auto()  # (= 3)
    # ImGuiInputSource_Clipboard,         /* original C++ signature */
    clipboard = enum.auto()  # (= 4)  # Currently only used by InputText()
    # ImGuiInputSource_COUNT    /* original C++ signature */
    # }
    count = enum.auto()  # (= 5)

# FIXME: Structures in the union below need to be declared as anonymous unions appears to be an extension?
# Using ImVec2() would fail on Clang 'union member 'MousePos' has a non-trivial default constructor'
class InputEventMousePos:
    # float PosX,     /* original C++ signature */
    pos_x: float
    # PosY;    /* original C++ signature */
    pos_y: float
    # ImGuiMouseSource MouseSource;    /* original C++ signature */
    mouse_source: MouseSource
    # ImGuiInputEventMousePos(float PosX = float(), float PosY = float(), ImGuiMouseSource MouseSource = ImGuiMouseSource());    /* original C++ signature */
    def __init__(
        self,
        pos_x: float = float(),
        pos_y: float = float(),
        mouse_source: MouseSource = MouseSource(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class InputEventMouseWheel:
    # float WheelX,     /* original C++ signature */
    wheel_x: float
    # WheelY;    /* original C++ signature */
    wheel_y: float
    # ImGuiMouseSource MouseSource;    /* original C++ signature */
    mouse_source: MouseSource
    # ImGuiInputEventMouseWheel(float WheelX = float(), float WheelY = float(), ImGuiMouseSource MouseSource = ImGuiMouseSource());    /* original C++ signature */
    def __init__(
        self,
        wheel_x: float = float(),
        wheel_y: float = float(),
        mouse_source: MouseSource = MouseSource(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class InputEventMouseButton:
    # int Button;    /* original C++ signature */
    button: int
    # bool Down;    /* original C++ signature */
    down: bool
    # ImGuiMouseSource MouseSource;    /* original C++ signature */
    mouse_source: MouseSource
    # ImGuiInputEventMouseButton(int Button = int(), bool Down = bool(), ImGuiMouseSource MouseSource = ImGuiMouseSource());    /* original C++ signature */
    def __init__(
        self,
        button: int = int(),
        down: bool = bool(),
        mouse_source: MouseSource = MouseSource(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class InputEventMouseViewport:
    # ImGuiID HoveredViewportID;    /* original C++ signature */
    hovered_viewport_id: ID
    # ImGuiInputEventMouseViewport(ImGuiID HoveredViewportID = ImGuiID());    /* original C++ signature */
    def __init__(self, hovered_viewport_id: ID = ID()) -> None:
        """Auto-generated default constructor with named params"""
        pass

class InputEventKey:
    # ImGuiKey Key;    /* original C++ signature */
    key: Key
    # bool Down;    /* original C++ signature */
    down: bool
    # float AnalogValue;    /* original C++ signature */
    analog_value: float
    # ImGuiInputEventKey(ImGuiKey Key = ImGuiKey(), bool Down = bool(), float AnalogValue = float());    /* original C++ signature */
    def __init__(
        self, key: Key = Key(), down: bool = bool(), analog_value: float = float()
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class InputEventText:
    # unsigned int Char;    /* original C++ signature */
    char: int
    # ImGuiInputEventText();    /* original C++ signature */
    def __init__(self) -> None:
        """Auto-generated default constructor"""
        pass

class InputEventAppFocused:
    # bool Focused;    /* original C++ signature */
    focused: bool
    # ImGuiInputEventAppFocused(bool Focused = bool());    /* original C++ signature */
    def __init__(self, focused: bool = bool()) -> None:
        """Auto-generated default constructor with named params"""
        pass

class InputEvent:
    # ImGuiInputEventType             Type;    /* original C++ signature */
    type: InputEventType
    # ImGuiInputSource                Source;    /* original C++ signature */
    source: InputSource
    # ImU32                           EventId;    /* original C++ signature */
    event_id: ImU32  # Unique, sequential increasing integer to identify an event (if you need to correlate them to other data).
    # bool                            AddedByTestEngine;    /* original C++ signature */
    added_by_test_engine: bool

    # ImGuiInputEvent() { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

# Input function taking an 'ImGuiID owner_id' argument defaults to (ImGuiKeyOwner_Any == 0) aka don't test ownership, which matches legacy behavior.

class KeyRoutingData:
    """Routing table entry (sizeof() == 16 bytes)"""

    # ImGuiKeyRoutingIndex            NextEntryIndex;    /* original C++ signature */
    next_entry_index: KeyRoutingIndex
    # ImU16                           Mods;    /* original C++ signature */
    mods: ImU16  # Technically we'd only need 4-bits but for simplify we store ImGuiMod_ values which need 16-bits. ImGuiMod_Shortcut is already translated to Ctrl/Super.
    # ImU8                            RoutingNextScore;    /* original C++ signature */
    routing_next_score: ImU8  # Lower is better (0: perfect score)
    # ImGuiID                         RoutingCurr;    /* original C++ signature */
    routing_curr: ID
    # ImGuiID                         RoutingNext;    /* original C++ signature */
    routing_next: ID

    # ImGuiKeyRoutingData()           { NextEntryIndex = -1; Mods = 0; RoutingNextScore = 255; RoutingCurr = RoutingNext = ImGuiKeyOwner_None; }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class KeyRoutingTable:
    """Routing table: maintain a desired owner for each possible key-chord (key + mods), and setup owner in NewFrame() when mods are matching.
    Stored in main context (1 instance)
    """

    # ImVector<ImGuiKeyRoutingData>   Entries;    /* original C++ signature */
    entries: ImVector_KeyRoutingData
    # ImVector<ImGuiKeyRoutingData>   EntriesNext;    /* original C++ signature */
    entries_next: ImVector_KeyRoutingData  # Double-buffer to avoid reallocation (could use a shared buffer)

    # ImGuiKeyRoutingTable()          { Clear(); }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # void Clear()                    { for (int n = 0; n < IM_ARRAYSIZE(Index); n++) Index[n] = -1; Entries.clear(); EntriesNext.clear(); }    /* original C++ signature */
    def clear(self) -> None:
        """(private API)"""
        pass

class KeyOwnerData:
    """This extends ImGuiKeyData but only for named keys (legacy keys don't support the new features)
    Stored in main context (1 per named key). In the future it might be merged into ImGuiKeyData.
    """

    # ImGuiID     OwnerCurr;    /* original C++ signature */
    owner_curr: ID
    # ImGuiID     OwnerNext;    /* original C++ signature */
    owner_next: ID
    # bool        LockThisFrame;    /* original C++ signature */
    lock_this_frame: bool  # Reading this key requires explicit owner id (until end of frame). Set by ImGuiInputFlags_LockThisFrame.
    # bool        LockUntilRelease;    /* original C++ signature */
    lock_until_release: bool  # Reading this key requires explicit owner id (until key is released). Set by ImGuiInputFlags_LockUntilRelease. When this is True LockThisFrame is always True as well.

    # ImGuiKeyOwnerData()             { OwnerCurr = OwnerNext = ImGuiKeyOwner_None; LockThisFrame = LockUntilRelease = false; }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class InputFlags_(enum.Enum):
    """Flags for extended versions of IsKeyPressed(), IsMouseClicked(), Shortcut(), SetKeyOwner(), SetItemKeyOwner()
    Don't mistake with ImGuiInputTextFlags! (for ImGui::InputText() function)
    """

    # Flags for IsKeyPressed(), IsMouseClicked(), Shortcut()
    # ImGuiInputFlags_None                = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiInputFlags_Repeat              = 1 << 0,       /* original C++ signature */
    repeat = (
        enum.auto()
    )  # (= 1 << 0)  # Return True on successive repeats. Default for legacy IsKeyPressed(). NOT Default for legacy IsMouseClicked(). MUST BE == 1.
    # ImGuiInputFlags_RepeatRateDefault   = 1 << 1,       /* original C++ signature */
    repeat_rate_default = enum.auto()  # (= 1 << 1)  # Repeat rate: Regular (default)
    # ImGuiInputFlags_RepeatRateNavMove   = 1 << 2,       /* original C++ signature */
    repeat_rate_nav_move = enum.auto()  # (= 1 << 2)  # Repeat rate: Fast
    # ImGuiInputFlags_RepeatRateNavTweak  = 1 << 3,       /* original C++ signature */
    repeat_rate_nav_tweak = enum.auto()  # (= 1 << 3)  # Repeat rate: Faster
    # ImGuiInputFlags_RepeatRateMask_     = ImGuiInputFlags_RepeatRateDefault | ImGuiInputFlags_RepeatRateNavMove | ImGuiInputFlags_RepeatRateNavTweak,    /* original C++ signature */
    repeat_rate_mask_ = (
        enum.auto()
    )  # (= InputFlags_RepeatRateDefault | InputFlags_RepeatRateNavMove | InputFlags_RepeatRateNavTweak)

    # Flags for SetItemKeyOwner()
    # ImGuiInputFlags_CondHovered         = 1 << 4,       /* original C++ signature */
    cond_hovered = (
        enum.auto()
    )  # (= 1 << 4)  # Only set if item is hovered (default to both)
    # ImGuiInputFlags_CondActive          = 1 << 5,       /* original C++ signature */
    cond_active = (
        enum.auto()
    )  # (= 1 << 5)  # Only set if item is active (default to both)
    # ImGuiInputFlags_CondDefault_        = ImGuiInputFlags_CondHovered | ImGuiInputFlags_CondActive,    /* original C++ signature */
    cond_default_ = enum.auto()  # (= InputFlags_CondHovered | InputFlags_CondActive)
    # ImGuiInputFlags_CondMask_           = ImGuiInputFlags_CondHovered | ImGuiInputFlags_CondActive,    /* original C++ signature */
    cond_mask_ = enum.auto()  # (= InputFlags_CondHovered | InputFlags_CondActive)

    # Flags for SetKeyOwner(), SetItemKeyOwner()
    # ImGuiInputFlags_LockThisFrame       = 1 << 6,       /* original C++ signature */
    lock_this_frame = (
        enum.auto()
    )  # (= 1 << 6)  # Access to key data will require EXPLICIT owner ID (ImGuiKeyOwner_Any/0 will NOT accepted for polling). Cleared at end of frame. This is useful to make input-owner-aware code steal keys from non-input-owner-aware code.
    # ImGuiInputFlags_LockUntilRelease    = 1 << 7,       /* original C++ signature */
    lock_until_release = (
        enum.auto()
    )  # (= 1 << 7)  # Access to key data will require EXPLICIT owner ID (ImGuiKeyOwner_Any/0 will NOT accepted for polling). Cleared when the key is released or at end of each frame if key is released. This is useful to make input-owner-aware code steal keys from non-input-owner-aware code.

    # Routing policies for Shortcut() + low-level SetShortcutRouting()
    # - The general idea is that several callers register interest in a shortcut, and only one owner gets it.
    # - When a policy (other than _RouteAlways) is set, Shortcut() will register itself with SetShortcutRouting(),
    #   allowing the system to decide where to route the input among other route-aware calls.
    # - Shortcut() uses ImGuiInputFlags_RouteFocused by default: meaning that a simple Shortcut() poll
    #   will register a route and only succeed when parent window is in the focus stack and if no-one
    #   with a higher priority is claiming the shortcut.
    # - Using ImGuiInputFlags_RouteAlways is roughly equivalent to doing e.g. IsKeyPressed(key) + testing mods.
    # - Priorities: GlobalHigh > Focused (when owner is active item) > Global > Focused (when focused window) > GlobalLow.
    # - Can select only 1 policy among all available.
    # ImGuiInputFlags_RouteFocused        = 1 << 8,       /* original C++ signature */
    route_focused = (
        enum.auto()
    )  # (= 1 << 8)  # (Default) Register focused route: Accept inputs if window is in focus stack. Deep-most focused window takes inputs. ActiveId takes inputs over deep-most focused window.
    # ImGuiInputFlags_RouteGlobalLow      = 1 << 9,       /* original C++ signature */
    route_global_low = (
        enum.auto()
    )  # (= 1 << 9)  # Register route globally (lowest priority: unless a focused window or active item registered the route) -> recommended Global priority.
    # ImGuiInputFlags_RouteGlobal         = 1 << 10,      /* original C++ signature */
    route_global = (
        enum.auto()
    )  # (= 1 << 10)  # Register route globally (medium priority: unless an active item registered the route, e.g. CTRL+A registered by InputText).
    # ImGuiInputFlags_RouteGlobalHigh     = 1 << 11,      /* original C++ signature */
    route_global_high = (
        enum.auto()
    )  # (= 1 << 11)  # Register route globally (highest priority: unlikely you need to use that: will interfere with every active items)
    # ImGuiInputFlags_RouteMask_          = ImGuiInputFlags_RouteFocused | ImGuiInputFlags_RouteGlobal | ImGuiInputFlags_RouteGlobalLow | ImGuiInputFlags_RouteGlobalHigh,     /* original C++ signature */
    route_mask_ = (
        enum.auto()
    )  # (= InputFlags_RouteFocused | InputFlags_RouteGlobal | InputFlags_RouteGlobalLow | InputFlags_RouteGlobalHigh)  # _Always not part of this!
    # ImGuiInputFlags_RouteAlways         = 1 << 12,      /* original C++ signature */
    route_always = (
        enum.auto()
    )  # (= 1 << 12)  # Do not register route, poll keys directly.
    # ImGuiInputFlags_RouteUnlessBgFocused= 1 << 13,      /* original C++ signature */
    route_unless_bg_focused = (
        enum.auto()
    )  # (= 1 << 13)  # Global routes will not be applied if underlying background/None is focused (== no Dear ImGui windows are focused). Useful for overlay applications.
    # ImGuiInputFlags_RouteExtraMask_     = ImGuiInputFlags_RouteAlways | ImGuiInputFlags_RouteUnlessBgFocused,    /* original C++ signature */
    route_extra_mask_ = (
        enum.auto()
    )  # (= InputFlags_RouteAlways | InputFlags_RouteUnlessBgFocused)

    # [Internal] Mask of which function support which flags
    # ImGuiInputFlags_SupportedByIsKeyPressed     = ImGuiInputFlags_Repeat | ImGuiInputFlags_RepeatRateMask_,    /* original C++ signature */
    supported_by_is_key_pressed = (
        enum.auto()
    )  # (= InputFlags_Repeat | InputFlags_RepeatRateMask_)
    # ImGuiInputFlags_SupportedByShortcut         = ImGuiInputFlags_Repeat | ImGuiInputFlags_RepeatRateMask_ | ImGuiInputFlags_RouteMask_ | ImGuiInputFlags_RouteExtraMask_,    /* original C++ signature */
    supported_by_shortcut = (
        enum.auto()
    )  # (= InputFlags_Repeat | InputFlags_RepeatRateMask_ | InputFlags_RouteMask_ | InputFlags_RouteExtraMask_)
    # ImGuiInputFlags_SupportedBySetKeyOwner      = ImGuiInputFlags_LockThisFrame | ImGuiInputFlags_LockUntilRelease,    /* original C++ signature */
    supported_by_set_key_owner = (
        enum.auto()
    )  # (= InputFlags_LockThisFrame | InputFlags_LockUntilRelease)
    # ImGuiInputFlags_SupportedBySetItemKeyOwner  = ImGuiInputFlags_SupportedBySetKeyOwner | ImGuiInputFlags_CondMask_,    /* original C++ signature */
    # }
    supported_by_set_item_key_owner = (
        enum.auto()
    )  # (= InputFlags_SupportedBySetKeyOwner | InputFlags_CondMask_)

# -----------------------------------------------------------------------------
# [SECTION] Clipper support
# -----------------------------------------------------------------------------

class ListClipperRange:
    """Note that Max is exclusive, so perhaps should be using a Begin/End convention."""

    # int     Min;    /* original C++ signature */
    min: int
    # int     Max;    /* original C++ signature */
    max: int
    # bool    PosToIndexConvert;    /* original C++ signature */
    pos_to_index_convert: bool  # Begin/End are absolute position (will be converted to indices later)
    # ImS8    PosToIndexOffsetMin;    /* original C++ signature */
    pos_to_index_offset_min: ImS8  # Add to Min after converting to indices
    # ImS8    PosToIndexOffsetMax;    /* original C++ signature */
    pos_to_index_offset_max: ImS8  # Add to Min after converting to indices

    # static ImGuiListClipperRange    FromIndices(int min, int max)                               { ImGuiListClipperRange r = { min, max, false, 0, 0 }; return r; }    /* original C++ signature */
    @staticmethod
    def from_indices(min: int, max: int) -> ListClipperRange:
        """(private API)"""
        pass
    # static ImGuiListClipperRange    FromPositions(float y1, float y2, int off_min, int off_max) { ImGuiListClipperRange r = { (int)y1, (int)y2, true, (ImS8)off_min, (ImS8)off_max }; return r; }    /* original C++ signature */
    @staticmethod
    def from_positions(
        y1: float, y2: float, off_min: int, off_max: int
    ) -> ListClipperRange:
        """(private API)"""
        pass
    # ImGuiListClipperRange(int Min = int(), int Max = int(), bool PosToIndexConvert = bool(), ImS8 PosToIndexOffsetMin = ImS8(), ImS8 PosToIndexOffsetMax = ImS8());    /* original C++ signature */
    def __init__(
        self,
        min: int = int(),
        max: int = int(),
        pos_to_index_convert: bool = bool(),
        pos_to_index_offset_min: ImS8 = ImS8(),
        pos_to_index_offset_max: ImS8 = ImS8(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class ListClipperData:
    """Temporary clipper data, buffers shared/reused between instances"""

    # ImGuiListClipper*               ListClipper;    /* original C++ signature */
    list_clipper: ListClipper
    # float                           LossynessOffset;    /* original C++ signature */
    lossyness_offset: float
    # int                             StepNo;    /* original C++ signature */
    step_no: int
    # int                             ItemsFrozen;    /* original C++ signature */
    items_frozen: int
    # ImVector<ImGuiListClipperRange> Ranges;    /* original C++ signature */
    ranges: ImVector_ListClipperRange

    # ImGuiListClipperData()          { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # void                            Reset(ImGuiListClipper* clipper) { ListClipper = clipper; StepNo = ItemsFrozen = 0; Ranges.resize(0); }    /* original C++ signature */
    def reset(self, clipper: ListClipper) -> None:
        """(private API)"""
        pass

# -----------------------------------------------------------------------------
# [SECTION] Navigation support
# -----------------------------------------------------------------------------

class ActivateFlags_(enum.Enum):
    # ImGuiActivateFlags_None                 = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiActivateFlags_PreferInput          = 1 << 0,           /* original C++ signature */
    prefer_input = (
        enum.auto()
    )  # (= 1 << 0)  # Favor activation that requires keyboard text input (e.g. for Slider/Drag). Default for Enter key.
    # ImGuiActivateFlags_PreferTweak          = 1 << 1,           /* original C++ signature */
    prefer_tweak = (
        enum.auto()
    )  # (= 1 << 1)  # Favor activation for tweaking with arrows or gamepad (e.g. for Slider/Drag). Default for Space key and if keyboard is not used.
    # ImGuiActivateFlags_TryToPreserveState   = 1 << 2,           /* original C++ signature */
    try_to_preserve_state = (
        enum.auto()
    )  # (= 1 << 2)  # Request widget to preserve state if it can (e.g. InputText will try to preserve cursor/selection)

class ScrollFlags_(enum.Enum):
    """Early work-in-progress API for ScrollToItem()"""

    # ImGuiScrollFlags_None                   = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiScrollFlags_KeepVisibleEdgeX       = 1 << 0,           /* original C++ signature */
    keep_visible_edge_x = (
        enum.auto()
    )  # (= 1 << 0)  # If item is not visible: scroll as little as possible on X axis to bring item back into view [default for X axis]
    # ImGuiScrollFlags_KeepVisibleEdgeY       = 1 << 1,           /* original C++ signature */
    keep_visible_edge_y = (
        enum.auto()
    )  # (= 1 << 1)  # If item is not visible: scroll as little as possible on Y axis to bring item back into view [default for Y axis for windows that are already visible]
    # ImGuiScrollFlags_KeepVisibleCenterX     = 1 << 2,           /* original C++ signature */
    keep_visible_center_x = (
        enum.auto()
    )  # (= 1 << 2)  # If item is not visible: scroll to make the item centered on X axis [rarely used]
    # ImGuiScrollFlags_KeepVisibleCenterY     = 1 << 3,           /* original C++ signature */
    keep_visible_center_y = (
        enum.auto()
    )  # (= 1 << 3)  # If item is not visible: scroll to make the item centered on Y axis
    # ImGuiScrollFlags_AlwaysCenterX          = 1 << 4,           /* original C++ signature */
    always_center_x = (
        enum.auto()
    )  # (= 1 << 4)  # Always center the result item on X axis [rarely used]
    # ImGuiScrollFlags_AlwaysCenterY          = 1 << 5,           /* original C++ signature */
    always_center_y = (
        enum.auto()
    )  # (= 1 << 5)  # Always center the result item on Y axis [default for Y axis for appearing window)
    # ImGuiScrollFlags_NoScrollParent         = 1 << 6,           /* original C++ signature */
    no_scroll_parent = (
        enum.auto()
    )  # (= 1 << 6)  # Disable forwarding scrolling to parent window if required to keep item/rect visible (only scroll window the function was applied to).
    # ImGuiScrollFlags_MaskX_                 = ImGuiScrollFlags_KeepVisibleEdgeX | ImGuiScrollFlags_KeepVisibleCenterX | ImGuiScrollFlags_AlwaysCenterX,    /* original C++ signature */
    mask_x_ = (
        enum.auto()
    )  # (= ScrollFlags_KeepVisibleEdgeX | ScrollFlags_KeepVisibleCenterX | ScrollFlags_AlwaysCenterX)
    # ImGuiScrollFlags_MaskY_                 = ImGuiScrollFlags_KeepVisibleEdgeY | ImGuiScrollFlags_KeepVisibleCenterY | ImGuiScrollFlags_AlwaysCenterY,    /* original C++ signature */
    # }
    mask_y_ = (
        enum.auto()
    )  # (= ScrollFlags_KeepVisibleEdgeY | ScrollFlags_KeepVisibleCenterY | ScrollFlags_AlwaysCenterY)

class NavHighlightFlags_(enum.Enum):
    # ImGuiNavHighlightFlags_None             = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiNavHighlightFlags_TypeDefault      = 1 << 0,    /* original C++ signature */
    type_default = enum.auto()  # (= 1 << 0)
    # ImGuiNavHighlightFlags_TypeThin         = 1 << 1,    /* original C++ signature */
    type_thin = enum.auto()  # (= 1 << 1)
    # ImGuiNavHighlightFlags_AlwaysDraw       = 1 << 2,           /* original C++ signature */
    always_draw = (
        enum.auto()
    )  # (= 1 << 2)  # Draw rectangular highlight if (g.NavId == id) _even_ when using the mouse.
    # ImGuiNavHighlightFlags_NoRounding       = 1 << 3,    /* original C++ signature */
    # }
    no_rounding = enum.auto()  # (= 1 << 3)

class NavMoveFlags_(enum.Enum):
    # ImGuiNavMoveFlags_None                  = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiNavMoveFlags_LoopX                 = 1 << 0,       /* original C++ signature */
    loop_x = enum.auto()  # (= 1 << 0)  # On failed request, restart from opposite side
    # ImGuiNavMoveFlags_LoopY                 = 1 << 1,    /* original C++ signature */
    loop_y = enum.auto()  # (= 1 << 1)
    # ImGuiNavMoveFlags_WrapX                 = 1 << 2,       /* original C++ signature */
    wrap_x = (
        enum.auto()
    )  # (= 1 << 2)  # On failed request, request from opposite side one line down (when NavDir==right) or one line up (when NavDir==left)
    # ImGuiNavMoveFlags_WrapY                 = 1 << 3,       /* original C++ signature */
    wrap_y = (
        enum.auto()
    )  # (= 1 << 3)  # This is not super useful but provided for completeness
    # ImGuiNavMoveFlags_WrapMask_             = ImGuiNavMoveFlags_LoopX | ImGuiNavMoveFlags_LoopY | ImGuiNavMoveFlags_WrapX | ImGuiNavMoveFlags_WrapY,    /* original C++ signature */
    wrap_mask_ = (
        enum.auto()
    )  # (= NavMoveFlags_LoopX | NavMoveFlags_LoopY | NavMoveFlags_WrapX | NavMoveFlags_WrapY)
    # ImGuiNavMoveFlags_AllowCurrentNavId     = 1 << 4,       /* original C++ signature */
    allow_current_nav_id = (
        enum.auto()
    )  # (= 1 << 4)  # Allow scoring and considering the current NavId as a move target candidate. This is used when the move source is offset (e.g. pressing PageDown actually needs to send a Up move request, if we are pressing PageDown from the bottom-most item we need to stay in place)
    # ImGuiNavMoveFlags_AlsoScoreVisibleSet   = 1 << 5,       /* original C++ signature */
    also_score_visible_set = (
        enum.auto()
    )  # (= 1 << 5)  # Store alternate result in NavMoveResultLocalVisible that only comprise elements that are already fully visible (used by PageUp/PageDown)
    # ImGuiNavMoveFlags_ScrollToEdgeY         = 1 << 6,       /* original C++ signature */
    scroll_to_edge_y = (
        enum.auto()
    )  # (= 1 << 6)  # Force scrolling to min/max (used by Home/End) // FIXME-NAV: Aim to remove or reword, probably unnecessary
    # ImGuiNavMoveFlags_Forwarded             = 1 << 7,    /* original C++ signature */
    forwarded = enum.auto()  # (= 1 << 7)
    # ImGuiNavMoveFlags_DebugNoResult         = 1 << 8,       /* original C++ signature */
    debug_no_result = (
        enum.auto()
    )  # (= 1 << 8)  # Dummy scoring for debug purpose, don't apply result
    # ImGuiNavMoveFlags_FocusApi              = 1 << 9,       /* original C++ signature */
    focus_api = (
        enum.auto()
    )  # (= 1 << 9)  # Requests from focus API can land/focus/activate items even if they are marked with _NoTabStop (see NavProcessItemForTabbingRequest() for details)
    # ImGuiNavMoveFlags_IsTabbing             = 1 << 10,      /* original C++ signature */
    is_tabbing = (
        enum.auto()
    )  # (= 1 << 10)  # == Focus + Activate if item is Inputable + DontChangeNavHighlight
    # ImGuiNavMoveFlags_IsPageMove            = 1 << 11,      /* original C++ signature */
    is_page_move = enum.auto()  # (= 1 << 11)  # Identify a PageDown/PageUp request.
    # ImGuiNavMoveFlags_Activate              = 1 << 12,      /* original C++ signature */
    activate = enum.auto()  # (= 1 << 12)  # Activate/select target item.
    # ImGuiNavMoveFlags_NoSelect              = 1 << 13,      /* original C++ signature */
    no_select = (
        enum.auto()
    )  # (= 1 << 13)  # Don't trigger selection by not setting g.NavJustMovedTo
    # ImGuiNavMoveFlags_NoSetNavHighlight     = 1 << 14,      /* original C++ signature */
    no_set_nav_highlight = (
        enum.auto()
    )  # (= 1 << 14)  # Do not alter the visible state of keyboard vs mouse nav highlight

class NavLayer(enum.Enum):
    # ImGuiNavLayer_Main  = 0,        /* original C++ signature */
    main = enum.auto()  # (= 0)  # Main scrolling layer
    # ImGuiNavLayer_Menu  = 1,        /* original C++ signature */
    menu = enum.auto()  # (= 1)  # Menu layer (access with Alt)
    # ImGuiNavLayer_COUNT    /* original C++ signature */
    # }
    count = enum.auto()  # (= 2)

class NavItemData:
    # ImGuiWindow*        Window;    /* original C++ signature */
    window: Window  # Init,Move    // Best candidate window (result->ItemWindow->RootWindowForNav == request->Window)
    # ImGuiID             ID;    /* original C++ signature */
    id_: ID  # Init,Move    // Best candidate item ID
    # ImGuiID             FocusScopeId;    /* original C++ signature */
    focus_scope_id: ID  # Init,Move    // Best candidate focus scope ID
    # ImRect              RectRel;    /* original C++ signature */
    rect_rel: ImRect  # Init,Move    // Best candidate bounding box in window relative space
    # ImGuiItemFlags      InFlags;    /* original C++ signature */
    in_flags: ItemFlags  # ????,Move    // Best candidate item flags
    # ImGuiSelectionUserData SelectionUserData;    /* original C++ signature */
    selection_user_data: SelectionUserData  # I+Mov    // Best candidate SetNextItemSelectionData() value.
    # float               DistBox;    /* original C++ signature */
    dist_box: float  #      Move    // Best candidate box distance to current NavId
    # float               DistCenter;    /* original C++ signature */
    dist_center: float  #      Move    // Best candidate center distance to current NavId
    # float               DistAxial;    /* original C++ signature */
    dist_axial: float  #      Move    // Best candidate axial distance to current NavId

    # ImGuiNavItemData()  { Clear(); }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # void Clear()        { Window = NULL; ID = FocusScopeId = 0; InFlags = 0; SelectionUserData = -1; DistBox = DistCenter = DistAxial = FLT_MAX; }    /* original C++ signature */
    def clear(self) -> None:
        """(private API)"""
        pass

# -----------------------------------------------------------------------------
# [SECTION] Typing-select support
# -----------------------------------------------------------------------------

class TypingSelectFlags_(enum.Enum):
    """Flags for GetTypingSelectRequest()"""

    # ImGuiTypingSelectFlags_None                 = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiTypingSelectFlags_AllowBackspace       = 1 << 0,       /* original C++ signature */
    allow_backspace = (
        enum.auto()
    )  # (= 1 << 0)  # Backspace to delete character inputs. If using: ensure GetTypingSelectRequest() is not called more than once per frame (filter by e.g. focus state)
    # ImGuiTypingSelectFlags_AllowSingleCharMode  = 1 << 1,       /* original C++ signature */
    allow_single_char_mode = (
        enum.auto()
    )  # (= 1 << 1)  # Allow "single char" search mode which is activated when pressing the same character multiple times.

class TypingSelectRequest:
    """Returned by GetTypingSelectRequest(), designed to eventually be public."""

    # ImGuiTypingSelectFlags  Flags;    /* original C++ signature */
    flags: TypingSelectFlags  # Flags passed to GetTypingSelectRequest()
    # int                     SearchBufferLen;    /* original C++ signature */
    search_buffer_len: int
    # const char*             SearchBuffer;    /* original C++ signature */
    search_buffer: str  # Search buffer contents (use full string. unless SingleCharMode is set, in which case use SingleCharSize). # (const)
    # bool                    SelectRequest;    /* original C++ signature */
    select_request: bool  # Set when buffer was modified this frame, requesting a selection.
    # bool                    SingleCharMode;    /* original C++ signature */
    single_char_mode: bool  # Notify when buffer contains same character repeated, to implement special mode. In this situation it preferred to not display any on-screen search indication.
    # ImS8                    SingleCharSize;    /* original C++ signature */
    single_char_size: ImS8  # Length in bytes of first letter codepoint (1 for ascii, 2-4 for UTF-8). If (SearchBufferLen==RepeatCharSize) only 1 letter has been input.
    # ImGuiTypingSelectRequest(ImGuiTypingSelectFlags Flags = ImGuiTypingSelectFlags(), int SearchBufferLen = int(), bool SelectRequest = bool(), bool SingleCharMode = bool(), ImS8 SingleCharSize = ImS8());    /* original C++ signature */
    def __init__(
        self,
        flags: TypingSelectFlags = TypingSelectFlags(),
        search_buffer_len: int = int(),
        select_request: bool = bool(),
        single_char_mode: bool = bool(),
        single_char_size: ImS8 = ImS8(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class TypingSelectState:
    """Storage for GetTypingSelectRequest()"""

    # ImGuiTypingSelectRequest Request;    /* original C++ signature */
    request: TypingSelectRequest  # User-facing data
    # ImGuiID         FocusScope;    /* original C++ signature */
    focus_scope: ID
    # int             LastRequestFrame = 0;    /* original C++ signature */
    last_request_frame: int = 0
    # float           LastRequestTime = 0.0f;    /* original C++ signature */
    last_request_time: float = 0.0
    # bool            SingleCharModeLock = false;    /* original C++ signature */
    single_char_mode_lock: bool = False  # After a certain single char repeat count we lock into SingleCharMode. Two benefits: 1) buffer never fill, 2) we can provide an immediate SingleChar mode without timer elapsing.

    # ImGuiTypingSelectState() { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # void            Clear()  { SearchBuffer[0] = 0; SingleCharModeLock = false; }     /* original C++ signature */
    def clear(self) -> None:
        """(private API)

        We preserve remaining data for easier debugging
        """
        pass

# -----------------------------------------------------------------------------
# [SECTION] Columns support
# -----------------------------------------------------------------------------

class OldColumnFlags_(enum.Enum):
    """Flags for internal's BeginColumns(). Prefix using BeginTable() nowadays!"""

    # ImGuiOldColumnFlags_None                    = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiOldColumnFlags_NoBorder                = 1 << 0,       /* original C++ signature */
    no_border = enum.auto()  # (= 1 << 0)  # Disable column dividers
    # ImGuiOldColumnFlags_NoResize                = 1 << 1,       /* original C++ signature */
    no_resize = (
        enum.auto()
    )  # (= 1 << 1)  # Disable resizing columns when clicking on the dividers
    # ImGuiOldColumnFlags_NoPreserveWidths        = 1 << 2,       /* original C++ signature */
    no_preserve_widths = (
        enum.auto()
    )  # (= 1 << 2)  # Disable column width preservation when adjusting columns
    # ImGuiOldColumnFlags_NoForceWithinWindow     = 1 << 3,       /* original C++ signature */
    no_force_within_window = (
        enum.auto()
    )  # (= 1 << 3)  # Disable forcing columns to fit within window
    # ImGuiOldColumnFlags_GrowParentContentsSize  = 1 << 4,       /* original C++ signature */
    grow_parent_contents_size = (
        enum.auto()
    )  # (= 1 << 4)  # (WIP) Restore pre-1.51 behavior of extending the parent window contents size but _without affecting the columns width at all_. Will eventually remove.

    # Obsolete names (will be removed)

class OldColumnData:
    # float               OffsetNorm;    /* original C++ signature */
    offset_norm: float  # Column start offset, normalized 0.0 (far left) -> 1.0 (far right)
    # float               OffsetNormBeforeResize;    /* original C++ signature */
    offset_norm_before_resize: float
    # ImGuiOldColumnFlags Flags;    /* original C++ signature */
    flags: OldColumnFlags  # Not exposed
    # ImRect              ClipRect;    /* original C++ signature */
    clip_rect: ImRect

    # ImGuiOldColumnData() { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class OldColumns:
    # ImGuiID             ID;    /* original C++ signature */
    id_: ID
    # ImGuiOldColumnFlags Flags;    /* original C++ signature */
    flags: OldColumnFlags
    # bool                IsFirstFrame;    /* original C++ signature */
    is_first_frame: bool
    # bool                IsBeingResized;    /* original C++ signature */
    is_being_resized: bool
    # int                 Current;    /* original C++ signature */
    current: int
    # int                 Count;    /* original C++ signature */
    count: int
    # float               OffMinX,     /* original C++ signature */
    off_min_x: float  # Offsets from HostWorkRect.Min.x
    # OffMaxX;    /* original C++ signature */
    off_max_x: float  # Offsets from HostWorkRect.Min.x
    # float               LineMinY,     /* original C++ signature */
    line_min_y: float
    # LineMaxY;    /* original C++ signature */
    line_max_y: float
    # float               HostCursorPosY;    /* original C++ signature */
    host_cursor_pos_y: float  # Backup of CursorPos at the time of BeginColumns()
    # float               HostCursorMaxPosX;    /* original C++ signature */
    host_cursor_max_pos_x: float  # Backup of CursorMaxPos at the time of BeginColumns()
    # ImRect              HostInitialClipRect;    /* original C++ signature */
    host_initial_clip_rect: ImRect  # Backup of ClipRect at the time of BeginColumns()
    # ImRect              HostBackupClipRect;    /* original C++ signature */
    host_backup_clip_rect: ImRect  # Backup of ClipRect during PushColumnsBackground()/PopColumnsBackground()
    # ImRect              HostBackupParentWorkRect;    /* original C++ signature */
    host_backup_parent_work_rect: ImRect  # Backup of WorkRect at the time of BeginColumns()
    # ImVector<ImGuiOldColumnData> Columns;    /* original C++ signature */
    columns: ImVector_OldColumnData
    # ImDrawListSplitter  Splitter;    /* original C++ signature */
    splitter: ImDrawListSplitter

    # ImGuiOldColumns()   { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

# -----------------------------------------------------------------------------
# [SECTION] Multi-select support
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# [SECTION] Docking support
# -----------------------------------------------------------------------------

# #ifdef IMGUI_HAS_DOCK
#

class DockNodeFlagsPrivate_(enum.Enum):
    """Extend ImGuiDockNodeFlags_"""

    # [Internal]
    # ImGuiDockNodeFlags_DockSpace                = 1 << 10,      /* original C++ signature */
    dock_space = (
        enum.auto()
    )  # (= 1 << 10)  # Saved // A dockspace is a node that occupy space within an existing user window. Otherwise the node is floating and create its own window.
    # ImGuiDockNodeFlags_CentralNode              = 1 << 11,      /* original C++ signature */
    central_node = (
        enum.auto()
    )  # (= 1 << 11)  # Saved // The central node has 2 main properties: stay visible when empty, only use "remaining" spaces from its neighbor.
    # ImGuiDockNodeFlags_NoTabBar                 = 1 << 12,      /* original C++ signature */
    no_tab_bar = (
        enum.auto()
    )  # (= 1 << 12)  # Saved // Tab bar is completely unavailable. No triangle in the corner to enable it back.
    # ImGuiDockNodeFlags_HiddenTabBar             = 1 << 13,      /* original C++ signature */
    hidden_tab_bar = (
        enum.auto()
    )  # (= 1 << 13)  # Saved // Tab bar is hidden, with a triangle in the corner to show it again (NB: actual tab-bar instance may be destroyed as this is only used for single-window tab bar)
    # ImGuiDockNodeFlags_NoWindowMenuButton       = 1 << 14,      /* original C++ signature */
    no_window_menu_button = (
        enum.auto()
    )  # (= 1 << 14)  # Saved // Disable window/docking menu (that one that appears instead of the collapse button)
    # ImGuiDockNodeFlags_NoCloseButton            = 1 << 15,      /* original C++ signature */
    no_close_button = enum.auto()  # (= 1 << 15)  # Saved // Disable close button
    # ImGuiDockNodeFlags_NoResizeX                = 1 << 16,      /* original C++ signature */
    no_resize_x = enum.auto()  # (= 1 << 16)  #       //
    # ImGuiDockNodeFlags_NoResizeY                = 1 << 17,      /* original C++ signature */
    no_resize_y = enum.auto()  # (= 1 << 17)  #       //
    # Disable docking/undocking actions in this dockspace or individual node (existing docked nodes will be preserved)
    # Those are not exposed in public because the desirable sharing/inheriting/copy-flag-on-split behaviors are quite difficult to design and understand.
    # The two public flags ImGuiDockNodeFlags_NoDockingOverCentralNode/ImGuiDockNodeFlags_NoDockingSplit don't have those issues.
    # ImGuiDockNodeFlags_NoDockingSplitOther      = 1 << 19,      /* original C++ signature */
    no_docking_split_other = (
        enum.auto()
    )  # (= 1 << 19)  #       // Disable this node from splitting other windows/nodes.
    # ImGuiDockNodeFlags_NoDockingOverMe          = 1 << 20,      /* original C++ signature */
    no_docking_over_me = (
        enum.auto()
    )  # (= 1 << 20)  #       // Disable other windows/nodes from being docked over this node.
    # ImGuiDockNodeFlags_NoDockingOverOther       = 1 << 21,      /* original C++ signature */
    no_docking_over_other = (
        enum.auto()
    )  # (= 1 << 21)  #       // Disable this node from being docked over another window or non-empty node.
    # ImGuiDockNodeFlags_NoDockingOverEmpty       = 1 << 22,      /* original C++ signature */
    no_docking_over_empty = (
        enum.auto()
    )  # (= 1 << 22)  #       // Disable this node from being docked over an empty node (e.g. DockSpace with no other windows)
    # ImGuiDockNodeFlags_NoDocking                = ImGuiDockNodeFlags_NoDockingOverMe | ImGuiDockNodeFlags_NoDockingOverOther | ImGuiDockNodeFlags_NoDockingOverEmpty | ImGuiDockNodeFlags_NoDockingSplit | ImGuiDockNodeFlags_NoDockingSplitOther,    /* original C++ signature */
    no_docking = (
        enum.auto()
    )  # (= DockNodeFlags_NoDockingOverMe | DockNodeFlags_NoDockingOverOther | DockNodeFlags_NoDockingOverEmpty | DockNodeFlags_NoDockingSplit | DockNodeFlags_NoDockingSplitOther)
    # Masks
    # ImGuiDockNodeFlags_SharedFlagsInheritMask_  = ~0,    /* original C++ signature */
    shared_flags_inherit_mask_ = enum.auto()  # (= ~0)
    # ImGuiDockNodeFlags_NoResizeFlagsMask_       = ImGuiDockNodeFlags_NoResize | ImGuiDockNodeFlags_NoResizeX | ImGuiDockNodeFlags_NoResizeY,    /* original C++ signature */
    no_resize_flags_mask_ = (
        enum.auto()
    )  # (= DockNodeFlags_NoResize | DockNodeFlags_NoResizeX | DockNodeFlags_NoResizeY)
    # When splitting, those local flags are moved to the inheriting child, never duplicated
    # ImGuiDockNodeFlags_LocalFlagsTransferMask_  = ImGuiDockNodeFlags_NoDockingSplit | ImGuiDockNodeFlags_NoResizeFlagsMask_ | ImGuiDockNodeFlags_AutoHideTabBar | ImGuiDockNodeFlags_CentralNode | ImGuiDockNodeFlags_NoTabBar | ImGuiDockNodeFlags_HiddenTabBar | ImGuiDockNodeFlags_NoWindowMenuButton | ImGuiDockNodeFlags_NoCloseButton,    /* original C++ signature */
    local_flags_transfer_mask_ = (
        enum.auto()
    )  # (= DockNodeFlags_NoDockingSplit | DockNodeFlags_NoResizeFlagsMask_ | DockNodeFlags_AutoHideTabBar | DockNodeFlags_CentralNode | DockNodeFlags_NoTabBar | DockNodeFlags_HiddenTabBar | DockNodeFlags_NoWindowMenuButton | DockNodeFlags_NoCloseButton)
    # ImGuiDockNodeFlags_SavedFlagsMask_          = ImGuiDockNodeFlags_NoResizeFlagsMask_ | ImGuiDockNodeFlags_DockSpace | ImGuiDockNodeFlags_CentralNode | ImGuiDockNodeFlags_NoTabBar | ImGuiDockNodeFlags_HiddenTabBar | ImGuiDockNodeFlags_NoWindowMenuButton | ImGuiDockNodeFlags_NoCloseButton,    /* original C++ signature */
    # }
    saved_flags_mask_ = (
        enum.auto()
    )  # (= DockNodeFlags_NoResizeFlagsMask_ | DockNodeFlags_DockSpace | DockNodeFlags_CentralNode | DockNodeFlags_NoTabBar | DockNodeFlags_HiddenTabBar | DockNodeFlags_NoWindowMenuButton | DockNodeFlags_NoCloseButton)

class DataAuthority_(enum.Enum):
    """Store the source authority (dock node vs window) of a field"""

    # ImGuiDataAuthority_Auto,    /* original C++ signature */
    auto = enum.auto()  # (= 0)
    # ImGuiDataAuthority_DockNode,    /* original C++ signature */
    dock_node = enum.auto()  # (= 1)
    # ImGuiDataAuthority_Window,    /* original C++ signature */
    # }
    window = enum.auto()  # (= 2)

class DockNodeState(enum.Enum):
    # ImGuiDockNodeState_Unknown,    /* original C++ signature */
    unknown = enum.auto()  # (= 0)
    # ImGuiDockNodeState_HostWindowHiddenBecauseSingleWindow,    /* original C++ signature */
    host_window_hidden_because_single_window = enum.auto()  # (= 1)
    # ImGuiDockNodeState_HostWindowHiddenBecauseWindowsAreResizing,    /* original C++ signature */
    host_window_hidden_because_windows_are_resizing = enum.auto()  # (= 2)
    # ImGuiDockNodeState_HostWindowVisible,    /* original C++ signature */
    # }
    host_window_visible = enum.auto()  # (= 3)

class DockNode:
    """sizeof() 156~192"""

    # ImGuiID                 ID;    /* original C++ signature */
    id_: ID
    # ImGuiDockNodeFlags      SharedFlags;    /* original C++ signature */
    shared_flags: DockNodeFlags  # (Write) Flags shared by all nodes of a same dockspace hierarchy (inherited from the root node)
    # ImGuiDockNodeFlags      LocalFlags;    /* original C++ signature */
    local_flags: DockNodeFlags  # (Write) Flags specific to this node
    # ImGuiDockNodeFlags      LocalFlagsInWindows;    /* original C++ signature */
    local_flags_in_windows: DockNodeFlags  # (Write) Flags specific to this node, applied from windows
    # ImGuiDockNodeFlags      MergedFlags;    /* original C++ signature */
    merged_flags: DockNodeFlags  # (Read)  Effective flags (== SharedFlags | LocalFlagsInNode | LocalFlagsInWindows)
    # ImGuiDockNodeState      State;    /* original C++ signature */
    state: DockNodeState
    # ImGuiDockNode*          ParentNode;    /* original C++ signature */
    parent_node: DockNode
    # ImVector<ImGuiWindow*>  Windows;    /* original C++ signature */
    windows: ImVector_Window_ptr  # Note: unordered list! Iterate TabBar->Tabs for user-order.
    # ImGuiTabBar*            TabBar;    /* original C++ signature */
    tab_bar: TabBar
    # ImVec2                  Pos;    /* original C++ signature */
    pos: ImVec2  # Current position
    # ImVec2                  Size;    /* original C++ signature */
    size: ImVec2  # Current size
    # ImVec2                  SizeRef;    /* original C++ signature */
    size_ref: ImVec2  # [Split node only] Last explicitly written-to size (overridden when using a splitter affecting the node), used to calculate Size.
    # ImGuiAxis               SplitAxis;    /* original C++ signature */
    split_axis: Axis  # [Split node only] Split axis (X or Y)
    # ImGuiWindowClass        WindowClass;    /* original C++ signature */
    window_class: WindowClass  # [Root node only]
    # ImU32                   LastBgColor;    /* original C++ signature */
    last_bg_color: ImU32

    # ImGuiWindow*            HostWindow;    /* original C++ signature */
    host_window: Window
    # ImGuiWindow*            VisibleWindow;    /* original C++ signature */
    visible_window: Window  # Generally point to window which is ID is == SelectedTabID, but when CTRL+Tabbing this can be a different window.
    # ImGuiDockNode*          CentralNode;    /* original C++ signature */
    central_node: DockNode  # [Root node only] Pointer to central node.
    # ImGuiDockNode*          OnlyNodeWithWindows;    /* original C++ signature */
    only_node_with_windows: DockNode  # [Root node only] Set when there is a single visible node within the hierarchy.
    # int                     CountNodeWithWindows;    /* original C++ signature */
    count_node_with_windows: int  # [Root node only]
    # int                     LastFrameAlive;    /* original C++ signature */
    last_frame_alive: int  # Last frame number the node was updated or kept alive explicitly with DockSpace() + ImGuiDockNodeFlags_KeepAliveOnly
    # int                     LastFrameActive;    /* original C++ signature */
    last_frame_active: int  # Last frame number the node was updated.
    # int                     LastFrameFocused;    /* original C++ signature */
    last_frame_focused: int  # Last frame number the node was focused.
    # ImGuiID                 LastFocusedNodeId;    /* original C++ signature */
    last_focused_node_id: ID  # [Root node only] Which of our child docking node (any ancestor in the hierarchy) was last focused.
    # ImGuiID                 SelectedTabId;    /* original C++ signature */
    selected_tab_id: ID  # [Leaf node only] Which of our tab/window is selected.
    # ImGuiID                 WantCloseTabId;    /* original C++ signature */
    want_close_tab_id: ID  # [Leaf node only] Set when closing a specific tab/window.
    # ImGuiID                 RefViewportId;    /* original C++ signature */
    ref_viewport_id: ID  # Reference viewport ID from visible window when HostWindow == None.

    # ImGuiDockNode(ImGuiID id);    /* original C++ signature */
    def __init__(self, id_: ID) -> None:
        pass
    # bool                    IsRootNode() const      { return ParentNode == NULL; }    /* original C++ signature */
    def is_root_node(self) -> bool:
        """(private API)"""
        pass
    # bool                    IsDockSpace() const     { return (MergedFlags & ImGuiDockNodeFlags_DockSpace) != 0; }    /* original C++ signature */
    def is_dock_space(self) -> bool:
        """(private API)"""
        pass
    # bool                    IsFloatingNode() const  { return ParentNode == NULL && (MergedFlags & ImGuiDockNodeFlags_DockSpace) == 0; }    /* original C++ signature */
    def is_floating_node(self) -> bool:
        """(private API)"""
        pass
    # bool                    IsCentralNode() const   { return (MergedFlags & ImGuiDockNodeFlags_CentralNode) != 0; }    /* original C++ signature */
    def is_central_node(self) -> bool:
        """(private API)"""
        pass
    # bool                    IsHiddenTabBar() const  { return (MergedFlags & ImGuiDockNodeFlags_HiddenTabBar) != 0; }     /* original C++ signature */
    def is_hidden_tab_bar(self) -> bool:
        """(private API)

        Hidden tab bar can be shown back by clicking the small triangle
        """
        pass
    # bool                    IsNoTabBar() const      { return (MergedFlags & ImGuiDockNodeFlags_NoTabBar) != 0; }         /* original C++ signature */
    def is_no_tab_bar(self) -> bool:
        """(private API)

        Never show a tab bar
        """
        pass
    # bool                    IsSplitNode() const     { return ChildNodes[0] != NULL; }    /* original C++ signature */
    def is_split_node(self) -> bool:
        """(private API)"""
        pass
    # bool                    IsLeafNode() const      { return ChildNodes[0] == NULL; }    /* original C++ signature */
    def is_leaf_node(self) -> bool:
        """(private API)"""
        pass
    # bool                    IsEmpty() const         { return ChildNodes[0] == NULL && Windows.Size == 0; }    /* original C++ signature */
    def is_empty(self) -> bool:
        """(private API)"""
        pass
    # ImRect                  Rect() const            { return ImRect(Pos.x, Pos.y, Pos.x + Size.x, Pos.y + Size.y); }    /* original C++ signature */
    def rect(self) -> ImRect:
        """(private API)"""
        pass
    # void                    SetLocalFlags(ImGuiDockNodeFlags flags) { LocalFlags = flags; UpdateMergedFlags(); }    /* original C++ signature */
    def set_local_flags(self, flags: DockNodeFlags) -> None:
        """(private API)"""
        pass
    # void                    UpdateMergedFlags()     { MergedFlags = SharedFlags | LocalFlags | LocalFlagsInWindows; }    /* original C++ signature */
    def update_merged_flags(self) -> None:
        """(private API)"""
        pass

class WindowDockStyleCol(enum.Enum):
    """List of colors that are stored at the time of Begin() into Docked Windows.
    We currently store the packed colors in a simple array window->DockStyle.Colors[].
    A better solution may involve appending into a log of colors in ImGuiContext + store offsets into those arrays in ImGuiWindow,
    but it would be more complex as we'd need to double-buffer both as e.g. drop target may refer to window from last frame.
    """

    # ImGuiWindowDockStyleCol_Text,    /* original C++ signature */
    text = enum.auto()  # (= 0)
    # ImGuiWindowDockStyleCol_Tab,    /* original C++ signature */
    tab = enum.auto()  # (= 1)
    # ImGuiWindowDockStyleCol_TabHovered,    /* original C++ signature */
    tab_hovered = enum.auto()  # (= 2)
    # ImGuiWindowDockStyleCol_TabActive,    /* original C++ signature */
    tab_active = enum.auto()  # (= 3)
    # ImGuiWindowDockStyleCol_TabUnfocused,    /* original C++ signature */
    tab_unfocused = enum.auto()  # (= 4)
    # ImGuiWindowDockStyleCol_TabUnfocusedActive,    /* original C++ signature */
    tab_unfocused_active = enum.auto()  # (= 5)
    # ImGuiWindowDockStyleCol_COUNT    /* original C++ signature */
    # }
    count = enum.auto()  # (= 6)

class WindowDockStyle:
    # ImGuiWindowDockStyle();    /* original C++ signature */
    def __init__(self) -> None:
        """Auto-generated default constructor"""
        pass

class DockContext:
    # ImGuiStorage                    Nodes;    /* original C++ signature */
    nodes: Storage  # Map ID -> ImGuiDockNode*: Active nodes
    # bool                            WantFullRebuild;    /* original C++ signature */
    want_full_rebuild: bool
    # ImGuiDockContext()              { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

# #endif

# -----------------------------------------------------------------------------
# [SECTION] Viewport support
# -----------------------------------------------------------------------------

class ViewportP:
    """ImGuiViewport Private/Internals fields (cardinal sin: we are using inheritance!)
    Every instance of ImGuiViewport is in fact a ImGuiViewportP.
    """

    # ImGuiWindow*        Window;    /* original C++ signature */
    window: Window  # Set when the viewport is owned by a window (and ImGuiViewportFlags_CanHostOtherWindows is NOT set)
    # int                 Idx;    /* original C++ signature */
    idx: int
    # int                 LastFrameActive;    /* original C++ signature */
    last_frame_active: int  # Last frame number this viewport was activated by a window
    # int                 LastFocusedStampCount;    /* original C++ signature */
    last_focused_stamp_count: int  # Last stamp number from when a window hosted by this viewport was focused (by comparing this value between two viewport we have an implicit viewport z-order we use as fallback)
    # ImGuiID             LastNameHash;    /* original C++ signature */
    last_name_hash: ID
    # ImVec2              LastPos;    /* original C++ signature */
    last_pos: ImVec2
    # float               Alpha;    /* original C++ signature */
    alpha: float  # Window opacity (when dragging dockable windows/viewports we make them transparent)
    # float               LastAlpha;    /* original C++ signature */
    last_alpha: float
    # bool                LastFocusedHadNavWindow;    /* original C++ signature */
    last_focused_had_nav_window: bool  # Instead of maintaining a LastFocusedWindow (which may harder to correctly maintain), we merely store weither NavWindow != None last time the viewport was focused.
    # short               PlatformMonitor;    /* original C++ signature */
    platform_monitor: int
    # int                 BgFgDrawListsLastFrame[2];    /* original C++ signature */
    bg_fg_draw_lists_last_frame: np.ndarray  # ndarray[type=int, size=2]  # Last frame number the background (0) and foreground (1) draw lists were used
    # ImDrawData          DrawDataP;    /* original C++ signature */
    draw_data_p: ImDrawData
    # ImDrawDataBuilder   DrawDataBuilder;    /* original C++ signature */
    draw_data_builder: ImDrawDataBuilder  # Temporary data while building final ImDrawData
    # ImVec2              LastPlatformPos;    /* original C++ signature */
    last_platform_pos: ImVec2
    # ImVec2              LastPlatformSize;    /* original C++ signature */
    last_platform_size: ImVec2
    # ImVec2              LastRendererSize;    /* original C++ signature */
    last_renderer_size: ImVec2
    # ImVec2              WorkOffsetMin;    /* original C++ signature */
    work_offset_min: ImVec2  # Work Area: Offset from Pos to top-left corner of Work Area. Generally (0,0) or (0,+main_menu_bar_height). Work Area is Full Area but without menu-bars/status-bars (so WorkArea always fit inside Pos/Size!)
    # ImVec2              WorkOffsetMax;    /* original C++ signature */
    work_offset_max: ImVec2  # Work Area: Offset from Pos+Size to bottom-right corner of Work Area. Generally (0,0) or (0,-status_bar_height).
    # ImVec2              BuildWorkOffsetMin;    /* original C++ signature */
    build_work_offset_min: ImVec2  # Work Area: Offset being built during current frame. Generally >= 0.0.
    # ImVec2              BuildWorkOffsetMax;    /* original C++ signature */
    build_work_offset_max: ImVec2  # Work Area: Offset being built during current frame. Generally <= 0.0.

    # ImGuiViewportP()                    { Window = NULL; Idx = -1; LastFrameActive = BgFgDrawListsLastFrame[0] = BgFgDrawListsLastFrame[1] = LastFocusedStampCount = -1; LastNameHash = 0; Alpha = LastAlpha = 1.0f; LastFocusedHadNavWindow = false; PlatformMonitor = -1; BgFgDrawLists[0] = BgFgDrawLists[1] = NULL; LastPlatformPos = LastPlatformSize = LastRendererSize = ImVec2(FLT_MAX, FLT_MAX); }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # void    ClearRequestFlags()         { PlatformRequestClose = PlatformRequestMove = PlatformRequestResize = false; }    /* original C++ signature */
    def clear_request_flags(self) -> None:
        """(private API)"""
        pass
    # Calculate work rect pos/size given a set of offset (we have 1 pair of offset for rect locked from last frame data, and 1 pair for currently building rect)
    # ImVec2  CalcWorkRectPos(const ImVec2& off_min) const                            { return ImVec2(Pos.x + off_min.x, Pos.y + off_min.y); }    /* original C++ signature */
    def calc_work_rect_pos(self, off_min: ImVec2) -> ImVec2:
        """(private API)"""
        pass
    # ImVec2  CalcWorkRectSize(const ImVec2& off_min, const ImVec2& off_max) const    { return ImVec2(ImMax(0.0f, Size.x - off_min.x + off_max.x), ImMax(0.0f, Size.y - off_min.y + off_max.y)); }    /* original C++ signature */
    def calc_work_rect_size(self, off_min: ImVec2, off_max: ImVec2) -> ImVec2:
        """(private API)"""
        pass
    # void    UpdateWorkRect()            { WorkPos = CalcWorkRectPos(WorkOffsetMin); WorkSize = CalcWorkRectSize(WorkOffsetMin, WorkOffsetMax); }     /* original C++ signature */
    def update_work_rect(self) -> None:
        """(private API)

        Update public fields
        """
        pass
    # Helpers to retrieve ImRect (we don't need to store BuildWorkRect as every access tend to change it, hence the code asymmetry)
    # ImRect  GetMainRect() const         { return ImRect(Pos.x, Pos.y, Pos.x + Size.x, Pos.y + Size.y); }    /* original C++ signature */
    def get_main_rect(self) -> ImRect:
        """(private API)"""
        pass
    # ImRect  GetWorkRect() const         { return ImRect(WorkPos.x, WorkPos.y, WorkPos.x + WorkSize.x, WorkPos.y + WorkSize.y); }    /* original C++ signature */
    def get_work_rect(self) -> ImRect:
        """(private API)"""
        pass
    # ImRect  GetBuildWorkRect() const    { ImVec2 pos = CalcWorkRectPos(BuildWorkOffsetMin); ImVec2 size = CalcWorkRectSize(BuildWorkOffsetMin, BuildWorkOffsetMax); return ImRect(pos.x, pos.y, pos.x + size.x, pos.y + size.y); }    /* original C++ signature */
    def get_build_work_rect(self) -> ImRect:
        """(private API)"""
        pass

# -----------------------------------------------------------------------------
# [SECTION] Settings support
# -----------------------------------------------------------------------------

class WindowSettings:
    """Windows data saved in imgui.ini file
    Because we never destroy or rename ImGuiWindowSettings, we can store the names in a separate buffer easily.
    (this is designed to be stored in a ImChunkStream buffer, with the variable-length Name following our structure)
    """

    # ImGuiID     ID;    /* original C++ signature */
    id_: ID
    # ImVec2ih    Pos;    /* original C++ signature */
    pos: ImVec2ih  # NB: Settings position are stored RELATIVE to the viewport! Whereas runtime ones are absolute positions.
    # ImVec2ih    Size;    /* original C++ signature */
    size: ImVec2ih
    # ImVec2ih    ViewportPos;    /* original C++ signature */
    viewport_pos: ImVec2ih
    # ImGuiID     ViewportId;    /* original C++ signature */
    viewport_id: ID
    # ImGuiID     DockId;    /* original C++ signature */
    dock_id: ID  # ID of last known DockNode (even if the DockNode is invisible because it has only 1 active window), or 0 if none.
    # ImGuiID     ClassId;    /* original C++ signature */
    class_id: ID  # ID of window class if specified
    # short       DockOrder;    /* original C++ signature */
    dock_order: int  # Order of the last time the window was visible within its DockNode. This is used to reorder windows that are reappearing on the same frame. Same value between windows that were active and windows that were none are possible.
    # bool        Collapsed;    /* original C++ signature */
    collapsed: bool
    # bool        IsChild;    /* original C++ signature */
    is_child: bool
    # bool        WantApply;    /* original C++ signature */
    want_apply: bool  # Set when loaded from .ini data (to enable merging/loading .ini data into an already running context)
    # bool        WantDelete;    /* original C++ signature */
    want_delete: bool  # Set to invalidate/delete the settings entry

    # ImGuiWindowSettings()       { memset(this, 0, sizeof(*this)); DockOrder = -1; }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # [ADAPT_IMGUI_BUNDLE]
    #                  #ifdef IMGUI_BUNDLE_PYTHON_API
    #
    # std::string GetNameStr()             { return std::string((const char*)(this + 1)); }    /* original C++ signature */
    def get_name_str(self) -> str:
        """(private API)"""
        pass
    #                  #endif
    #
    # [/ADAPT_IMGUI_BUNDLE]

class SettingsHandler:
    # const char* TypeName;    /* original C++ signature */
    type_name: str  # Short description stored in .ini file. Disallowed characters: '[' ']' # (const)
    # ImGuiID     TypeHash;    /* original C++ signature */
    type_hash: ID  # == ImHashStr(TypeName)
    # void*       UserData;    /* original C++ signature */
    user_data: Any

    # ImGuiSettingsHandler() { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

# -----------------------------------------------------------------------------
# [SECTION] Localization support
# -----------------------------------------------------------------------------

class LocKey(enum.Enum):
    """This is experimental and not officially supported, it'll probably fall short of features, if/when it does we may backtrack."""

    # ImGuiLocKey_VersionStr,    /* original C++ signature */
    version_str = enum.auto()  # (= 0)
    # ImGuiLocKey_TableSizeOne,    /* original C++ signature */
    table_size_one = enum.auto()  # (= 1)
    # ImGuiLocKey_TableSizeAllFit,    /* original C++ signature */
    table_size_all_fit = enum.auto()  # (= 2)
    # ImGuiLocKey_TableSizeAllDefault,    /* original C++ signature */
    table_size_all_default = enum.auto()  # (= 3)
    # ImGuiLocKey_TableResetOrder,    /* original C++ signature */
    table_reset_order = enum.auto()  # (= 4)
    # ImGuiLocKey_WindowingMainMenuBar,    /* original C++ signature */
    windowing_main_menu_bar = enum.auto()  # (= 5)
    # ImGuiLocKey_WindowingPopup,    /* original C++ signature */
    windowing_popup = enum.auto()  # (= 6)
    # ImGuiLocKey_WindowingUntitled,    /* original C++ signature */
    windowing_untitled = enum.auto()  # (= 7)
    # ImGuiLocKey_DockingHideTabBar,    /* original C++ signature */
    docking_hide_tab_bar = enum.auto()  # (= 8)
    # ImGuiLocKey_DockingHoldShiftToDock,    /* original C++ signature */
    docking_hold_shift_to_dock = enum.auto()  # (= 9)
    # ImGuiLocKey_DockingDragToUndockOrMoveNode,    /* original C++ signature */
    docking_drag_to_undock_or_move_node = enum.auto()  # (= 10)
    # ImGuiLocKey_COUNT    /* original C++ signature */
    # }
    count = enum.auto()  # (= 11)

class LocEntry:
    # ImGuiLocKey     Key;    /* original C++ signature */
    key: LocKey
    # const char*     Text;    /* original C++ signature */
    text: str  # (const)
    # ImGuiLocEntry(ImGuiLocKey Key = ImGuiLocKey());    /* original C++ signature */
    def __init__(self, key: LocKey = LocKey()) -> None:
        """Auto-generated default constructor with named params"""
        pass

# -----------------------------------------------------------------------------
# [SECTION] Metrics, Debug Tools
# -----------------------------------------------------------------------------

class DebugLogFlags_(enum.Enum):
    # Event types
    # ImGuiDebugLogFlags_None             = 0,    /* original C++ signature */
    none = enum.auto()  # (= 0)
    # ImGuiDebugLogFlags_EventActiveId    = 1 << 0,    /* original C++ signature */
    event_active_id = enum.auto()  # (= 1 << 0)
    # ImGuiDebugLogFlags_EventFocus       = 1 << 1,    /* original C++ signature */
    event_focus = enum.auto()  # (= 1 << 1)
    # ImGuiDebugLogFlags_EventPopup       = 1 << 2,    /* original C++ signature */
    event_popup = enum.auto()  # (= 1 << 2)
    # ImGuiDebugLogFlags_EventNav         = 1 << 3,    /* original C++ signature */
    event_nav = enum.auto()  # (= 1 << 3)
    # ImGuiDebugLogFlags_EventClipper     = 1 << 4,    /* original C++ signature */
    event_clipper = enum.auto()  # (= 1 << 4)
    # ImGuiDebugLogFlags_EventSelection   = 1 << 5,    /* original C++ signature */
    event_selection = enum.auto()  # (= 1 << 5)
    # ImGuiDebugLogFlags_EventIO          = 1 << 6,    /* original C++ signature */
    event_io = enum.auto()  # (= 1 << 6)
    # ImGuiDebugLogFlags_EventDocking     = 1 << 7,    /* original C++ signature */
    event_docking = enum.auto()  # (= 1 << 7)
    # ImGuiDebugLogFlags_EventViewport    = 1 << 8,    /* original C++ signature */
    event_viewport = enum.auto()  # (= 1 << 8)
    # ImGuiDebugLogFlags_EventMask_       = ImGuiDebugLogFlags_EventActiveId | ImGuiDebugLogFlags_EventFocus | ImGuiDebugLogFlags_EventPopup | ImGuiDebugLogFlags_EventNav | ImGuiDebugLogFlags_EventClipper | ImGuiDebugLogFlags_EventSelection | ImGuiDebugLogFlags_EventIO | ImGuiDebugLogFlags_EventDocking | ImGuiDebugLogFlags_EventViewport,    /* original C++ signature */
    event_mask_ = (
        enum.auto()
    )  # (= DebugLogFlags_EventActiveId | DebugLogFlags_EventFocus | DebugLogFlags_EventPopup | DebugLogFlags_EventNav | DebugLogFlags_EventClipper | DebugLogFlags_EventSelection | DebugLogFlags_EventIO | DebugLogFlags_EventDocking | DebugLogFlags_EventViewport)
    # ImGuiDebugLogFlags_OutputToTTY      = 1 << 10,      /* original C++ signature */
    output_to_tty = enum.auto()  # (= 1 << 10)  # Also send output to TTY
    # ImGuiDebugLogFlags_OutputToTestEngine = 1 << 11,    /* original C++ signature */
    output_to_test_engine = (
        enum.auto()
    )  # (= 1 << 11)  # Also send output to Test Engine

class DebugAllocEntry:
    # int         FrameCount;    /* original C++ signature */
    frame_count: int
    # ImS16       AllocCount;    /* original C++ signature */
    alloc_count: ImS16
    # ImS16       FreeCount;    /* original C++ signature */
    free_count: ImS16
    # ImGuiDebugAllocEntry(int FrameCount = int(), ImS16 AllocCount = ImS16(), ImS16 FreeCount = ImS16());    /* original C++ signature */
    def __init__(
        self,
        frame_count: int = int(),
        alloc_count: ImS16 = ImS16(),
        free_count: ImS16 = ImS16(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class DebugAllocInfo:
    # int         TotalAllocCount;    /* original C++ signature */
    total_alloc_count: int  # Number of call to MemAlloc().
    # int         TotalFreeCount;    /* original C++ signature */
    total_free_count: int
    # ImS16       LastEntriesIdx;    /* original C++ signature */
    last_entries_idx: ImS16  # Current index in buffer

    # ImGuiDebugAllocInfo() { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class MetricsConfig:
    # bool        ShowDebugLog = false;    /* original C++ signature */
    show_debug_log: bool = False
    # bool        ShowIDStackTool = false;    /* original C++ signature */
    show_id_stack_tool: bool = False
    # bool        ShowWindowsRects = false;    /* original C++ signature */
    show_windows_rects: bool = False
    # bool        ShowWindowsBeginOrder = false;    /* original C++ signature */
    show_windows_begin_order: bool = False
    # bool        ShowTablesRects = false;    /* original C++ signature */
    show_tables_rects: bool = False
    # bool        ShowDrawCmdMesh = true;    /* original C++ signature */
    show_draw_cmd_mesh: bool = True
    # bool        ShowDrawCmdBoundingBoxes = true;    /* original C++ signature */
    show_draw_cmd_bounding_boxes: bool = True
    # bool        ShowAtlasTintedWithTextColor = false;    /* original C++ signature */
    show_atlas_tinted_with_text_color: bool = False
    # bool        ShowDockingNodes = false;    /* original C++ signature */
    show_docking_nodes: bool = False
    # int         ShowWindowsRectsType = -1;    /* original C++ signature */
    show_windows_rects_type: int = -1
    # int         ShowTablesRectsType = -1;    /* original C++ signature */
    show_tables_rects_type: int = -1
    # ImGuiMetricsConfig(bool ShowDebugLog = false, bool ShowIDStackTool = false, bool ShowWindowsRects = false, bool ShowWindowsBeginOrder = false, bool ShowTablesRects = false, bool ShowDrawCmdMesh = true, bool ShowDrawCmdBoundingBoxes = true, bool ShowAtlasTintedWithTextColor = false, bool ShowDockingNodes = false, int ShowWindowsRectsType = -1, int ShowTablesRectsType = -1);    /* original C++ signature */
    def __init__(
        self,
        show_debug_log: bool = False,
        show_id_stack_tool: bool = False,
        show_windows_rects: bool = False,
        show_windows_begin_order: bool = False,
        show_tables_rects: bool = False,
        show_draw_cmd_mesh: bool = True,
        show_draw_cmd_bounding_boxes: bool = True,
        show_atlas_tinted_with_text_color: bool = False,
        show_docking_nodes: bool = False,
        show_windows_rects_type: int = -1,
        show_tables_rects_type: int = -1,
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class StackLevelInfo:
    # ImGuiID                 ID;    /* original C++ signature */
    id_: ID
    # ImS8                    QueryFrameCount;    /* original C++ signature */
    query_frame_count: ImS8  # >= 1: Query in progress
    # bool                    QuerySuccess;    /* original C++ signature */
    query_success: bool  # Obtained result from DebugHookIdInfo()

    # ImGuiStackLevelInfo()   { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class IDStackTool:
    """State for ID Stack tool queries"""

    # int                     LastActiveFrame;    /* original C++ signature */
    last_active_frame: int
    # int                     StackLevel;    /* original C++ signature */
    stack_level: int  # -1: query stack and resize Results, >= 0: individual stack level
    # ImGuiID                 QueryId;    /* original C++ signature */
    query_id: ID  # ID to query details for
    # ImVector<ImGuiStackLevelInfo> Results;    /* original C++ signature */
    results: ImVector_StackLevelInfo
    # bool                    CopyToClipboardOnCtrlC;    /* original C++ signature */
    copy_to_clipboard_on_ctrl_c: bool
    # float                   CopyToClipboardLastTime;    /* original C++ signature */
    copy_to_clipboard_last_time: float

    # ImGuiIDStackTool()      { memset(this, 0, sizeof(*this)); CopyToClipboardLastTime = -FLT_MAX; }    /* original C++ signature */
    def __init__(self) -> None:
        pass

# -----------------------------------------------------------------------------
# [SECTION] Generic context hooks
# -----------------------------------------------------------------------------

class ContextHookType(enum.Enum):
    # ImGuiContextHookType_NewFramePre,     /* original C++ signature */
    new_frame_pre = enum.auto()  # (= 0)
    # ImGuiContextHookType_NewFramePost,     /* original C++ signature */
    new_frame_post = enum.auto()  # (= 1)
    # ImGuiContextHookType_EndFramePre,     /* original C++ signature */
    end_frame_pre = enum.auto()  # (= 2)
    # ImGuiContextHookType_EndFramePost,     /* original C++ signature */
    end_frame_post = enum.auto()  # (= 3)
    # ImGuiContextHookType_RenderPre,     /* original C++ signature */
    render_pre = enum.auto()  # (= 4)
    # ImGuiContextHookType_RenderPost,     /* original C++ signature */
    render_post = enum.auto()  # (= 5)
    # ImGuiContextHookType_Shutdown,     /* original C++ signature */
    shutdown = enum.auto()  # (= 6)
    # ImGuiContextHookType_PendingRemoval_ }    /* original C++ signature */
    pending_removal_ = enum.auto()  # (= 7)

class ContextHook:
    # ImGuiID                     HookId;    /* original C++ signature */
    hook_id: ID  # A unique ID assigned by AddContextHook()
    # ImGuiContextHookType        Type;    /* original C++ signature */
    type: ContextHookType
    # ImGuiID                     Owner;    /* original C++ signature */
    owner: ID
    # void*                       UserData;    /* original C++ signature */
    user_data: Any

    # ImGuiContextHook()          { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

# -----------------------------------------------------------------------------
# [SECTION] ImGuiContext (main Dear ImGui context)
# -----------------------------------------------------------------------------

class Context:
    # bool                    Initialized;    /* original C++ signature */
    initialized: bool
    # bool                    FontAtlasOwnedByContext;    /* original C++ signature */
    font_atlas_owned_by_context: bool  # IO.Fonts-> is owned by the ImGuiContext and will be destructed along with it.
    # ImGuiIO                 IO;    /* original C++ signature */
    io: IO
    # ImGuiPlatformIO         PlatformIO;    /* original C++ signature */
    platform_io: PlatformIO
    # ImGuiStyle              Style;    /* original C++ signature */
    style: Style
    # ImGuiConfigFlags        ConfigFlagsCurrFrame;    /* original C++ signature */
    config_flags_curr_frame: ConfigFlags  # = g.IO.ConfigFlags at the time of NewFrame()
    # ImGuiConfigFlags        ConfigFlagsLastFrame;    /* original C++ signature */
    config_flags_last_frame: ConfigFlags
    # ImFont*                 Font;    /* original C++ signature */
    font: ImFont  # (Shortcut) == FontStack.empty() ? IO.Font : FontStack.back()
    # float                   FontSize;    /* original C++ signature */
    font_size: float  # (Shortcut) == FontBaseSize * g.CurrentWindow->FontWindowScale == window->FontSize(). Text height for current window.
    # float                   FontBaseSize;    /* original C++ signature */
    font_base_size: float  # (Shortcut) == IO.FontGlobalScale * Font->Scale * Font->FontSize. Base text height.
    # ImDrawListSharedData    DrawListSharedData;    /* original C++ signature */
    draw_list_shared_data: ImDrawListSharedData
    # double                  Time;    /* original C++ signature */
    time: float
    # int                     FrameCount;    /* original C++ signature */
    frame_count: int
    # int                     FrameCountEnded;    /* original C++ signature */
    frame_count_ended: int
    # int                     FrameCountPlatformEnded;    /* original C++ signature */
    frame_count_platform_ended: int
    # int                     FrameCountRendered;    /* original C++ signature */
    frame_count_rendered: int
    # bool                    WithinFrameScope;    /* original C++ signature */
    within_frame_scope: bool  # Set by NewFrame(), cleared by EndFrame()
    # bool                    WithinFrameScopeWithImplicitWindow;    /* original C++ signature */
    within_frame_scope_with_implicit_window: bool  # Set by NewFrame(), cleared by EndFrame() when the implicit debug window has been pushed
    # bool                    WithinEndChild;    /* original C++ signature */
    within_end_child: bool  # Set within EndChild()
    # bool                    GcCompactAll;    /* original C++ signature */
    gc_compact_all: bool  # Request full GC
    # bool                    TestEngineHookItems;    /* original C++ signature */
    test_engine_hook_items: bool  # Will call test engine hooks: ImGuiTestEngineHook_ItemAdd(), ImGuiTestEngineHook_ItemInfo(), ImGuiTestEngineHook_Log()
    # void*                   TestEngine;    /* original C++ signature */
    test_engine: Any  # Test engine user data

    # Inputs
    # ImVector<ImGuiInputEvent> InputEventsQueue;    /* original C++ signature */
    input_events_queue: ImVector_InputEvent  # Input events which will be trickled/written into IO structure.
    # ImVector<ImGuiInputEvent> InputEventsTrail;    /* original C++ signature */
    input_events_trail: ImVector_InputEvent  # Past input events processed in NewFrame(). This is to allow domain-specific application to access e.g mouse/pen trail.
    # ImGuiMouseSource        InputEventsNextMouseSource;    /* original C++ signature */
    input_events_next_mouse_source: MouseSource
    # ImU32                   InputEventsNextEventId;    /* original C++ signature */
    input_events_next_event_id: ImU32

    # Windows state
    # ImVector<ImGuiWindow*>  Windows;    /* original C++ signature */
    windows: ImVector_Window_ptr  # Windows, sorted in display order, back to front
    # ImVector<ImGuiWindow*>  WindowsFocusOrder;    /* original C++ signature */
    windows_focus_order: ImVector_Window_ptr  # Root windows, sorted in focus order, back to front.
    # ImVector<ImGuiWindow*>  WindowsTempSortBuffer;    /* original C++ signature */
    windows_temp_sort_buffer: ImVector_Window_ptr  # Temporary buffer used in EndFrame() to reorder windows so parents are kept before their child
    # ImVector<ImGuiWindowStackData> CurrentWindowStack;    /* original C++ signature */
    current_window_stack: ImVector_WindowStackData
    # ImGuiStorage            WindowsById;    /* original C++ signature */
    windows_by_id: Storage  # Map window's ImGuiID to ImGuiWindow*
    # int                     WindowsActiveCount;    /* original C++ signature */
    windows_active_count: int  # Number of unique windows submitted by frame
    # ImVec2                  WindowsHoverPadding;    /* original C++ signature */
    windows_hover_padding: ImVec2  # Padding around resizable windows for which hovering on counts as hovering the window == ImMax(style.TouchExtraPadding, WINDOWS_HOVER_PADDING)
    # ImGuiWindow*            CurrentWindow;    /* original C++ signature */
    current_window: Window  # Window being drawn into
    # ImGuiWindow*            HoveredWindow;    /* original C++ signature */
    hovered_window: Window  # Window the mouse is hovering. Will typically catch mouse inputs.
    # ImGuiWindow*            HoveredWindowUnderMovingWindow;    /* original C++ signature */
    hovered_window_under_moving_window: Window  # Hovered window ignoring MovingWindow. Only set if MovingWindow is set.
    # ImGuiWindow*            MovingWindow;    /* original C++ signature */
    moving_window: Window  # Track the window we clicked on (in order to preserve focus). The actual window that is moved is generally MovingWindow->RootWindowDockTree.
    # ImGuiWindow*            WheelingWindow;    /* original C++ signature */
    wheeling_window: Window  # Track the window we started mouse-wheeling on. Until a timer elapse or mouse has moved, generally keep scrolling the same window even if during the course of scrolling the mouse ends up hovering a child window.
    # ImVec2                  WheelingWindowRefMousePos;    /* original C++ signature */
    wheeling_window_ref_mouse_pos: ImVec2
    # int                     WheelingWindowStartFrame;    /* original C++ signature */
    wheeling_window_start_frame: int  # This may be set one frame before WheelingWindow is != None
    # int                     WheelingWindowScrolledFrame;    /* original C++ signature */
    wheeling_window_scrolled_frame: int
    # float                   WheelingWindowReleaseTimer;    /* original C++ signature */
    wheeling_window_release_timer: float
    # ImVec2                  WheelingWindowWheelRemainder;    /* original C++ signature */
    wheeling_window_wheel_remainder: ImVec2
    # ImVec2                  WheelingAxisAvg;    /* original C++ signature */
    wheeling_axis_avg: ImVec2

    # Item/widgets state and tracking information
    # ImGuiID                 DebugHookIdInfo;    /* original C++ signature */
    debug_hook_id_info: ID  # Will call core hooks: DebugHookIdInfo() from GetID functions, used by ID Stack Tool [next HoveredId/ActiveId to not pull in an extra cache-line]
    # ImGuiID                 HoveredId;    /* original C++ signature */
    hovered_id: ID  # Hovered widget, filled during the frame
    # ImGuiID                 HoveredIdPreviousFrame;    /* original C++ signature */
    hovered_id_previous_frame: ID
    # bool                    HoveredIdAllowOverlap;    /* original C++ signature */
    hovered_id_allow_overlap: bool
    # bool                    HoveredIdDisabled;    /* original C++ signature */
    hovered_id_disabled: bool  # At least one widget passed the rect test, but has been discarded by disabled flag or popup inhibit. May be True even if HoveredId == 0.
    # float                   HoveredIdTimer;    /* original C++ signature */
    hovered_id_timer: float  # Measure contiguous hovering time
    # float                   HoveredIdNotActiveTimer;    /* original C++ signature */
    hovered_id_not_active_timer: float  # Measure contiguous hovering time where the item has not been active
    # ImGuiID                 ActiveId;    /* original C++ signature */
    active_id: ID  # Active widget
    # ImGuiID                 ActiveIdIsAlive;    /* original C++ signature */
    active_id_is_alive: ID  # Active widget has been seen this frame (we can't use a bool as the ActiveId may change within the frame)
    # float                   ActiveIdTimer;    /* original C++ signature */
    active_id_timer: float
    # bool                    ActiveIdIsJustActivated;    /* original C++ signature */
    active_id_is_just_activated: bool  # Set at the time of activation for one frame
    # bool                    ActiveIdAllowOverlap;    /* original C++ signature */
    active_id_allow_overlap: bool  # Active widget allows another widget to steal active id (generally for overlapping widgets, but not always)
    # bool                    ActiveIdNoClearOnFocusLoss;    /* original C++ signature */
    active_id_no_clear_on_focus_loss: bool  # Disable losing active id if the active id window gets unfocused.
    # bool                    ActiveIdHasBeenPressedBefore;    /* original C++ signature */
    active_id_has_been_pressed_before: bool  # Track whether the active id led to a press (this is to allow changing between PressOnClick and PressOnRelease without pressing twice). Used by range_select branch.
    # bool                    ActiveIdHasBeenEditedBefore;    /* original C++ signature */
    active_id_has_been_edited_before: bool  # Was the value associated to the widget Edited over the course of the Active state.
    # bool                    ActiveIdHasBeenEditedThisFrame;    /* original C++ signature */
    active_id_has_been_edited_this_frame: bool
    # ImVec2                  ActiveIdClickOffset;    /* original C++ signature */
    active_id_click_offset: ImVec2  # Clicked offset from upper-left corner, if applicable (currently only set by ButtonBehavior)
    # ImGuiWindow*            ActiveIdWindow;    /* original C++ signature */
    active_id_window: Window
    # ImGuiInputSource        ActiveIdSource;    /* original C++ signature */
    active_id_source: InputSource  # Activating source: ImGuiInputSource_Mouse OR ImGuiInputSource_Keyboard OR ImGuiInputSource_Gamepad
    # int                     ActiveIdMouseButton;    /* original C++ signature */
    active_id_mouse_button: int
    # ImGuiID                 ActiveIdPreviousFrame;    /* original C++ signature */
    active_id_previous_frame: ID
    # bool                    ActiveIdPreviousFrameIsAlive;    /* original C++ signature */
    active_id_previous_frame_is_alive: bool
    # bool                    ActiveIdPreviousFrameHasBeenEditedBefore;    /* original C++ signature */
    active_id_previous_frame_has_been_edited_before: bool
    # ImGuiWindow*            ActiveIdPreviousFrameWindow;    /* original C++ signature */
    active_id_previous_frame_window: Window
    # ImGuiID                 LastActiveId;    /* original C++ signature */
    last_active_id: ID  # Store the last non-zero ActiveId, useful for animation.
    # float                   LastActiveIdTimer;    /* original C++ signature */
    last_active_id_timer: float  # Store the last non-zero ActiveId timer since the beginning of activation, useful for animation.

    # [EXPERIMENTAL] Key/Input Ownership + Shortcut Routing system
    # - The idea is that instead of "eating" a given key, we can link to an owner.
    # - Input query can then read input by specifying ImGuiKeyOwner_Any (== 0), ImGuiKeyOwner_None (== -1) or a custom ID.
    # - Routing is requested ahead of time for a given chord (Key + Mods) and granted in NewFrame().
    # ImGuiKeyRoutingTable    KeysRoutingTable;    /* original C++ signature */
    keys_routing_table: KeyRoutingTable
    # ImU32                   ActiveIdUsingNavDirMask;    /* original C++ signature */
    active_id_using_nav_dir_mask: ImU32  # Active widget will want to read those nav move requests (e.g. can activate a button and move away from it)
    # bool                    ActiveIdUsingAllKeyboardKeys;    /* original C++ signature */
    active_id_using_all_keyboard_keys: bool
    # Active widget will want to read all keyboard keys inputs. (FIXME: This is a shortcut for not taking ownership of 100+ keys but perhaps best to not have the inconsistency)

    # Next window/item data
    # ImGuiID                 CurrentFocusScopeId;    /* original C++ signature */
    current_focus_scope_id: ID  # == g.FocusScopeStack.back()
    # ImGuiItemFlags          CurrentItemFlags;    /* original C++ signature */
    current_item_flags: ItemFlags  # == g.ItemFlagsStack.back()
    # ImGuiID                 DebugLocateId;    /* original C++ signature */
    debug_locate_id: ID  # Storage for DebugLocateItemOnHover() feature: this is read by ItemAdd() so we keep it in a hot/cached location
    # ImGuiNextItemData       NextItemData;    /* original C++ signature */
    next_item_data: NextItemData  # Storage for SetNextItem** functions
    # ImGuiLastItemData       LastItemData;    /* original C++ signature */
    last_item_data: LastItemData  # Storage for last submitted item (setup by ItemAdd)
    # ImGuiNextWindowData     NextWindowData;    /* original C++ signature */
    next_window_data: NextWindowData  # Storage for SetNextWindow** functions
    # bool                    DebugShowGroupRects;    /* original C++ signature */
    debug_show_group_rects: bool

    # Shared stacks
    # ImVector<ImGuiColorMod>     ColorStack;    /* original C++ signature */
    color_stack: ImVector_ColorMod  # Stack for PushStyleColor()/PopStyleColor() - inherited by Begin()
    # ImVector<ImGuiStyleMod>     StyleVarStack;    /* original C++ signature */
    style_var_stack: ImVector_StyleMod  # Stack for PushStyleVar()/PopStyleVar() - inherited by Begin()
    # ImVector<ImFont*>           FontStack;    /* original C++ signature */
    font_stack: ImVector_ImFont_ptr  # Stack for PushFont()/PopFont() - inherited by Begin()
    # ImVector<ImGuiID>           FocusScopeStack;    /* original C++ signature */
    focus_scope_stack: ImVector_ID  # Stack for PushFocusScope()/PopFocusScope() - inherited by BeginChild(), pushed into by Begin()
    # ImVector<ImGuiItemFlags>    ItemFlagsStack;    /* original C++ signature */
    item_flags_stack: ImVector_ItemFlags  # Stack for PushItemFlag()/PopItemFlag() - inherited by Begin()
    # ImVector<ImGuiGroupData>    GroupStack;    /* original C++ signature */
    group_stack: ImVector_GroupData  # Stack for BeginGroup()/EndGroup() - not inherited by Begin()
    # ImVector<ImGuiPopupData>    OpenPopupStack;    /* original C++ signature */
    open_popup_stack: ImVector_PopupData  # Which popups are open (persistent)
    # ImVector<ImGuiPopupData>    BeginPopupStack;    /* original C++ signature */
    begin_popup_stack: ImVector_PopupData  # Which level of BeginPopup() we are in (reset every frame)
    # ImVector<ImGuiNavTreeNodeData> NavTreeNodeStack;    /* original C++ signature */
    nav_tree_node_stack: ImVector_NavTreeNodeData  # Stack for TreeNode() when a NavLeft requested is emitted.

    # int                     BeginMenuCount;    /* original C++ signature */
    begin_menu_count: int

    # Viewports
    # ImVector<ImGuiViewportP*> Viewports;    /* original C++ signature */
    viewports: ImVector_ViewportP_ptr  # Active viewports (always 1+, and generally 1 unless multi-viewports are enabled). Each viewports hold their copy of ImDrawData.
    # float                   CurrentDpiScale;    /* original C++ signature */
    current_dpi_scale: float  # == CurrentViewport->DpiScale
    # ImGuiViewportP*         CurrentViewport;    /* original C++ signature */
    current_viewport: ViewportP  # We track changes of viewport (happening in Begin) so we can call Platform_OnChangedViewport()
    # ImGuiViewportP*         MouseViewport;    /* original C++ signature */
    mouse_viewport: ViewportP
    # ImGuiViewportP*         MouseLastHoveredViewport;    /* original C++ signature */
    mouse_last_hovered_viewport: ViewportP  # Last known viewport that was hovered by mouse (even if we are not hovering any viewport any more) + honoring the _NoInputs flag.
    # ImGuiID                 PlatformLastFocusedViewportId;    /* original C++ signature */
    platform_last_focused_viewport_id: ID
    # ImGuiPlatformMonitor    FallbackMonitor;    /* original C++ signature */
    fallback_monitor: PlatformMonitor  # Virtual monitor used as fallback if backend doesn't provide monitor information.
    # int                     ViewportCreatedCount;    /* original C++ signature */
    viewport_created_count: int  # Unique sequential creation counter (mostly for testing/debugging)
    # int                     PlatformWindowsCreatedCount;    /* original C++ signature */
    platform_windows_created_count: int  # Unique sequential creation counter (mostly for testing/debugging)
    # int                     ViewportFocusedStampCount;    /* original C++ signature */
    viewport_focused_stamp_count: int  # Every time the front-most window changes, we stamp its viewport with an incrementing counter

    # Gamepad/keyboard Navigation
    # ImGuiWindow*            NavWindow;    /* original C++ signature */
    nav_window: Window  # Focused window for navigation. Could be called 'FocusedWindow'
    # ImGuiID                 NavId;    /* original C++ signature */
    nav_id: ID  # Focused item for navigation
    # ImGuiID                 NavFocusScopeId;    /* original C++ signature */
    nav_focus_scope_id: ID  # Identify a selection scope (selection code often wants to "clear other items" when landing on an item of the selection set)
    # ImGuiID                 NavActivateId;    /* original C++ signature */
    nav_activate_id: ID  # ~~ (g.ActiveId == 0) && (IsKeyPressed(ImGuiKey_Space) || IsKeyDown(ImGuiKey_Enter) || IsKeyPressed(ImGuiKey_NavGamepadActivate)) ? NavId : 0, also set when calling ActivateItem()
    # ImGuiID                 NavActivateDownId;    /* original C++ signature */
    nav_activate_down_id: ID  # ~~ IsKeyDown(ImGuiKey_Space) || IsKeyDown(ImGuiKey_Enter) || IsKeyDown(ImGuiKey_NavGamepadActivate) ? NavId : 0
    # ImGuiID                 NavActivatePressedId;    /* original C++ signature */
    nav_activate_pressed_id: ID  # ~~ IsKeyPressed(ImGuiKey_Space) || IsKeyPressed(ImGuiKey_Enter) || IsKeyPressed(ImGuiKey_NavGamepadActivate) ? NavId : 0 (no repeat)
    # ImGuiActivateFlags      NavActivateFlags;    /* original C++ signature */
    nav_activate_flags: ActivateFlags
    # ImGuiID                 NavJustMovedToId;    /* original C++ signature */
    nav_just_moved_to_id: ID  # Just navigated to this id (result of a successfully MoveRequest).
    # ImGuiID                 NavJustMovedToFocusScopeId;    /* original C++ signature */
    nav_just_moved_to_focus_scope_id: ID  # Just navigated to this focus scope id (result of a successfully MoveRequest).
    # ImGuiKeyChord           NavJustMovedToKeyMods;    /* original C++ signature */
    nav_just_moved_to_key_mods: KeyChord
    # ImGuiID                 NavNextActivateId;    /* original C++ signature */
    nav_next_activate_id: ID  # Set by ActivateItem(), queued until next frame.
    # ImGuiActivateFlags      NavNextActivateFlags;    /* original C++ signature */
    nav_next_activate_flags: ActivateFlags
    # ImGuiInputSource        NavInputSource;    /* original C++ signature */
    nav_input_source: InputSource  # Keyboard or Gamepad mode? THIS CAN ONLY BE ImGuiInputSource_Keyboard or ImGuiInputSource_Mouse
    # ImGuiNavLayer           NavLayer;    /* original C++ signature */
    nav_layer: NavLayer  # Layer we are navigating on. For now the system is hard-coded for 0=main contents and 1=menu/title bar, may expose layers later.
    # ImGuiSelectionUserData  NavLastValidSelectionUserData;    /* original C++ signature */
    nav_last_valid_selection_user_data: SelectionUserData  # Last valid data passed to SetNextItemSelectionUser(), or -1. For current window. Not reset when focusing an item that doesn't have selection data.
    # bool                    NavIdIsAlive;    /* original C++ signature */
    nav_id_is_alive: bool  # Nav widget has been seen this frame ~~ NavRectRel is valid
    # bool                    NavMousePosDirty;    /* original C++ signature */
    nav_mouse_pos_dirty: bool  # When set we will update mouse position if (io.ConfigFlags & ImGuiConfigFlags_NavEnableSetMousePos) if set (NB: this not enabled by default)
    # bool                    NavDisableHighlight;    /* original C++ signature */
    nav_disable_highlight: bool  # When user starts using mouse, we hide gamepad/keyboard highlight (NB: but they are still available, which is why NavDisableHighlight isn't always != NavDisableMouseHover)
    # bool                    NavDisableMouseHover;    /* original C++ signature */
    nav_disable_mouse_hover: bool  # When user starts using gamepad/keyboard, we hide mouse hovering highlight until mouse is touched again.

    # Navigation: Init & Move Requests
    # bool                    NavAnyRequest;    /* original C++ signature */
    nav_any_request: bool  # ~~ NavMoveRequest || NavInitRequest this is to perform early out in ItemAdd()
    # bool                    NavInitRequest;    /* original C++ signature */
    nav_init_request: bool  # Init request for appearing window to select first item
    # bool                    NavInitRequestFromMove;    /* original C++ signature */
    nav_init_request_from_move: bool
    # ImGuiNavItemData        NavInitResult;    /* original C++ signature */
    nav_init_result: NavItemData  # Init request result (first item of the window, or one for which SetItemDefaultFocus() was called)
    # bool                    NavMoveSubmitted;    /* original C++ signature */
    nav_move_submitted: bool  # Move request submitted, will process result on next NewFrame()
    # bool                    NavMoveScoringItems;    /* original C++ signature */
    nav_move_scoring_items: bool  # Move request submitted, still scoring incoming items
    # bool                    NavMoveForwardToNextFrame;    /* original C++ signature */
    nav_move_forward_to_next_frame: bool
    # ImGuiNavMoveFlags       NavMoveFlags;    /* original C++ signature */
    nav_move_flags: NavMoveFlags
    # ImGuiScrollFlags        NavMoveScrollFlags;    /* original C++ signature */
    nav_move_scroll_flags: ScrollFlags
    # ImGuiKeyChord           NavMoveKeyMods;    /* original C++ signature */
    nav_move_key_mods: KeyChord
    # ImGuiDir                NavMoveDir;    /* original C++ signature */
    nav_move_dir: Dir  # Direction of the move request (left/right/up/down)
    # ImGuiDir                NavMoveDirForDebug;    /* original C++ signature */
    nav_move_dir_for_debug: Dir
    # ImGuiDir                NavMoveClipDir;    /* original C++ signature */
    nav_move_clip_dir: Dir  # FIXME-NAV: Describe the purpose of this better. Might want to rename?
    # ImRect                  NavScoringRect;    /* original C++ signature */
    nav_scoring_rect: ImRect  # Rectangle used for scoring, in screen space. Based of window->NavRectRel[], modified for directional navigation scoring.
    # ImRect                  NavScoringNoClipRect;    /* original C++ signature */
    nav_scoring_no_clip_rect: ImRect  # Some nav operations (such as PageUp/PageDown) enforce a region which clipper will attempt to always keep submitted
    # int                     NavScoringDebugCount;    /* original C++ signature */
    nav_scoring_debug_count: int  # Metrics for debugging
    # int                     NavTabbingDir;    /* original C++ signature */
    nav_tabbing_dir: int  # Generally -1 or +1, 0 when tabbing without a nav id
    # int                     NavTabbingCounter;    /* original C++ signature */
    nav_tabbing_counter: int  # >0 when counting items for tabbing
    # ImGuiNavItemData        NavMoveResultLocal;    /* original C++ signature */
    nav_move_result_local: NavItemData  # Best move request candidate within NavWindow
    # ImGuiNavItemData        NavMoveResultLocalVisible;    /* original C++ signature */
    nav_move_result_local_visible: NavItemData  # Best move request candidate within NavWindow that are mostly visible (when using ImGuiNavMoveFlags_AlsoScoreVisibleSet flag)
    # ImGuiNavItemData        NavMoveResultOther;    /* original C++ signature */
    nav_move_result_other: NavItemData  # Best move request candidate within NavWindow's flattened hierarchy (when using ImGuiWindowFlags_NavFlattened flag)
    # ImGuiNavItemData        NavTabbingResultFirst;    /* original C++ signature */
    nav_tabbing_result_first: NavItemData  # First tabbing request candidate within NavWindow and flattened hierarchy

    # Navigation: Windowing (CTRL+TAB for list, or Menu button + keys or directional pads to move/resize)
    # ImGuiKeyChord           ConfigNavWindowingKeyNext;    /* original C++ signature */
    config_nav_windowing_key_next: KeyChord  # = ImGuiMod_Ctrl | ImGuiKey_Tab, for reconfiguration (see #4828)
    # ImGuiKeyChord           ConfigNavWindowingKeyPrev;    /* original C++ signature */
    config_nav_windowing_key_prev: KeyChord  # = ImGuiMod_Ctrl | ImGuiMod_Shift | ImGuiKey_Tab
    # ImGuiWindow*            NavWindowingTarget;    /* original C++ signature */
    nav_windowing_target: Window  # Target window when doing CTRL+Tab (or Pad Menu + FocusPrev/Next), this window is temporarily displayed top-most!
    # ImGuiWindow*            NavWindowingTargetAnim;    /* original C++ signature */
    nav_windowing_target_anim: Window  # Record of last valid NavWindowingTarget until DimBgRatio and NavWindowingHighlightAlpha becomes 0.0, so the fade-out can stay on it.
    # ImGuiWindow*            NavWindowingListWindow;    /* original C++ signature */
    nav_windowing_list_window: Window  # Internal window actually listing the CTRL+Tab contents
    # float                   NavWindowingTimer;    /* original C++ signature */
    nav_windowing_timer: float
    # float                   NavWindowingHighlightAlpha;    /* original C++ signature */
    nav_windowing_highlight_alpha: float
    # bool                    NavWindowingToggleLayer;    /* original C++ signature */
    nav_windowing_toggle_layer: bool
    # ImVec2                  NavWindowingAccumDeltaPos;    /* original C++ signature */
    nav_windowing_accum_delta_pos: ImVec2
    # ImVec2                  NavWindowingAccumDeltaSize;    /* original C++ signature */
    nav_windowing_accum_delta_size: ImVec2

    # Render
    # float                   DimBgRatio;    /* original C++ signature */
    dim_bg_ratio: float  # 0.0..1.0 animation when fading in a dimming background (for modal window and CTRL+TAB list)

    # Drag and Drop
    # bool                    DragDropActive;    /* original C++ signature */
    drag_drop_active: bool
    # bool                    DragDropWithinSource;    /* original C++ signature */
    drag_drop_within_source: bool  # Set when within a BeginDragDropXXX/EndDragDropXXX block for a drag source.
    # bool                    DragDropWithinTarget;    /* original C++ signature */
    drag_drop_within_target: bool  # Set when within a BeginDragDropXXX/EndDragDropXXX block for a drag target.
    # ImGuiDragDropFlags      DragDropSourceFlags;    /* original C++ signature */
    drag_drop_source_flags: DragDropFlags
    # int                     DragDropSourceFrameCount;    /* original C++ signature */
    drag_drop_source_frame_count: int
    # int                     DragDropMouseButton;    /* original C++ signature */
    drag_drop_mouse_button: int
    # ImGuiPayload            DragDropPayload;    /* original C++ signature */
    drag_drop_payload: Payload
    # ImRect                  DragDropTargetRect;    /* original C++ signature */
    drag_drop_target_rect: ImRect  # Store rectangle of current target candidate (we favor small targets when overlapping)
    # ImGuiID                 DragDropTargetId;    /* original C++ signature */
    drag_drop_target_id: ID
    # ImGuiDragDropFlags      DragDropAcceptFlags;    /* original C++ signature */
    drag_drop_accept_flags: DragDropFlags
    # float                   DragDropAcceptIdCurrRectSurface;    /* original C++ signature */
    drag_drop_accept_id_curr_rect_surface: float  # Target item surface (we resolve overlapping targets by prioritizing the smaller surface)
    # ImGuiID                 DragDropAcceptIdCurr;    /* original C++ signature */
    drag_drop_accept_id_curr: ID  # Target item id (set at the time of accepting the payload)
    # ImGuiID                 DragDropAcceptIdPrev;    /* original C++ signature */
    drag_drop_accept_id_prev: ID  # Target item id from previous frame (we need to store this to allow for overlapping drag and drop targets)
    # int                     DragDropAcceptFrameCount;    /* original C++ signature */
    drag_drop_accept_frame_count: int  # Last time a target expressed a desire to accept the source
    # ImGuiID                 DragDropHoldJustPressedId;    /* original C++ signature */
    drag_drop_hold_just_pressed_id: ID  # Set when holding a payload just made ButtonBehavior() return a press.
    # ImVector<uchar> DragDropPayloadBufHeap;    /* original C++ signature */
    drag_drop_payload_buf_heap: ImVector_uchar  # We don't expose the ImVector<> directly, ImGuiPayload only holds pointer+size

    # Clipper
    # int                             ClipperTempDataStacked;    /* original C++ signature */
    clipper_temp_data_stacked: int
    # ImVector<ImGuiListClipperData>  ClipperTempData;    /* original C++ signature */
    clipper_temp_data: ImVector_ListClipperData

    # Tables
    # ImGuiTable*                     CurrentTable;    /* original C++ signature */
    current_table: Table
    # int                             TablesTempDataStacked;    /* original C++ signature */
    tables_temp_data_stacked: int  # Temporary table data size (because we leave previous instances undestructed, we generally don't use TablesTempData.Size)
    # ImVector<ImGuiTableTempData>    TablesTempData;    /* original C++ signature */
    tables_temp_data: ImVector_TableTempData  # Temporary table data (buffers reused/shared across instances, support nesting)
    # ImVector<float>                 TablesLastTimeActive;    /* original C++ signature */
    tables_last_time_active: ImVector_float  # Last used timestamp of each tables (SOA, for efficient GC)
    # ImVector<ImDrawChannel>         DrawChannelsTempMergeBuffer;    /* original C++ signature */
    draw_channels_temp_merge_buffer: ImVector_ImDrawChannel

    # Tab bars
    # ImGuiTabBar*                    CurrentTabBar;    /* original C++ signature */
    current_tab_bar: TabBar
    # ImVector<ImGuiPtrOrIndex>       CurrentTabBarStack;    /* original C++ signature */
    current_tab_bar_stack: ImVector_PtrOrIndex
    # ImVector<ImGuiShrinkWidthItem>  ShrinkWidthBuffer;    /* original C++ signature */
    shrink_width_buffer: ImVector_ShrinkWidthItem

    # Hover Delay system
    # ImGuiID                 HoverItemDelayId;    /* original C++ signature */
    hover_item_delay_id: ID
    # ImGuiID                 HoverItemDelayIdPreviousFrame;    /* original C++ signature */
    hover_item_delay_id_previous_frame: ID
    # float                   HoverItemDelayTimer;    /* original C++ signature */
    hover_item_delay_timer: float  # Currently used by IsItemHovered()
    # float                   HoverItemDelayClearTimer;    /* original C++ signature */
    hover_item_delay_clear_timer: float  # Currently used by IsItemHovered(): grace time before g.TooltipHoverTimer gets cleared.
    # ImGuiID                 HoverItemUnlockedStationaryId;    /* original C++ signature */
    hover_item_unlocked_stationary_id: ID  # Mouse has once been stationary on this item. Only reset after departing the item.
    # ImGuiID                 HoverWindowUnlockedStationaryId;    /* original C++ signature */
    hover_window_unlocked_stationary_id: ID  # Mouse has once been stationary on this window. Only reset after departing the window.

    # Mouse state
    # ImGuiMouseCursor        MouseCursor;    /* original C++ signature */
    mouse_cursor: MouseCursor
    # float                   MouseStationaryTimer;    /* original C++ signature */
    mouse_stationary_timer: float  # Time the mouse has been stationary (with some loose heuristic)
    # ImVec2                  MouseLastValidPos;    /* original C++ signature */
    mouse_last_valid_pos: ImVec2

    # Widget state
    # ImGuiInputTextState     InputTextState;    /* original C++ signature */
    input_text_state: InputTextState
    # ImGuiInputTextDeactivatedState InputTextDeactivatedState;    /* original C++ signature */
    input_text_deactivated_state: InputTextDeactivatedState
    # ImFont                  InputTextPasswordFont;    /* original C++ signature */
    input_text_password_font: ImFont
    # ImGuiID                 TempInputId;    /* original C++ signature */
    temp_input_id: ID  # Temporary text input when CTRL+clicking on a slider, etc.
    # ImGuiColorEditFlags     ColorEditOptions;    /* original C++ signature */
    color_edit_options: ColorEditFlags  # Store user options for color edit widgets
    # ImGuiID                 ColorEditCurrentID;    /* original C++ signature */
    color_edit_current_id: ID  # Set temporarily while inside of the parent-most ColorEdit4/ColorPicker4 (because they call each others).
    # ImGuiID                 ColorEditSavedID;    /* original C++ signature */
    color_edit_saved_id: ID  # ID we are saving/restoring HS for
    # float                   ColorEditSavedHue;    /* original C++ signature */
    color_edit_saved_hue: float  # Backup of last Hue associated to LastColor, so we can restore Hue in lossy RGB<>HSV round trips
    # float                   ColorEditSavedSat;    /* original C++ signature */
    color_edit_saved_sat: float  # Backup of last Saturation associated to LastColor, so we can restore Saturation in lossy RGB<>HSV round trips
    # ImU32                   ColorEditSavedColor;    /* original C++ signature */
    color_edit_saved_color: ImU32  # RGB value with alpha set to 0.
    # ImVec4                  ColorPickerRef;    /* original C++ signature */
    color_picker_ref: ImVec4  # Initial/reference color at the time of opening the color picker.
    # ImGuiComboPreviewData   ComboPreviewData;    /* original C++ signature */
    combo_preview_data: ComboPreviewData
    # ImRect                  WindowResizeBorderExpectedRect;    /* original C++ signature */
    window_resize_border_expected_rect: ImRect  # Expected border rect, switch to relative edit if moving
    # bool                    WindowResizeRelativeMode;    /* original C++ signature */
    window_resize_relative_mode: bool
    # float                   SliderGrabClickOffset;    /* original C++ signature */
    slider_grab_click_offset: float
    # float                   SliderCurrentAccum;    /* original C++ signature */
    slider_current_accum: float  # Accumulated slider delta when using navigation controls.
    # bool                    SliderCurrentAccumDirty;    /* original C++ signature */
    slider_current_accum_dirty: bool  # Has the accumulated slider delta changed since last time we tried to apply it?
    # bool                    DragCurrentAccumDirty;    /* original C++ signature */
    drag_current_accum_dirty: bool
    # float                   DragCurrentAccum;    /* original C++ signature */
    drag_current_accum: float  # Accumulator for dragging modification. Always high-precision, not rounded by end-user precision settings
    # float                   DragSpeedDefaultRatio;    /* original C++ signature */
    drag_speed_default_ratio: float  # If speed == 0.0, uses (max-min) * DragSpeedDefaultRatio
    # float                   ScrollbarClickDeltaToGrabCenter;    /* original C++ signature */
    scrollbar_click_delta_to_grab_center: float  # Distance between mouse and center of grab box, normalized in parent space. Use storage?
    # float                   DisabledAlphaBackup;    /* original C++ signature */
    disabled_alpha_backup: float  # Backup for style.Alpha for BeginDisabled()
    # short                   DisabledStackSize;    /* original C++ signature */
    disabled_stack_size: int
    # short                   LockMarkEdited;    /* original C++ signature */
    lock_mark_edited: int
    # short                   TooltipOverrideCount;    /* original C++ signature */
    tooltip_override_count: int
    # ImVector<char>          ClipboardHandlerData;    /* original C++ signature */
    clipboard_handler_data: ImVector_char  # If no custom clipboard handler is defined
    # ImVector<ImGuiID>       MenusIdSubmittedThisFrame;    /* original C++ signature */
    menus_id_submitted_this_frame: ImVector_ID  # A list of menu IDs that were rendered at least once
    # ImGuiTypingSelectState  TypingSelectState;    /* original C++ signature */
    typing_select_state: TypingSelectState  # State for GetTypingSelectRequest()

    # Platform support
    # ImGuiPlatformImeData    PlatformImeData;    /* original C++ signature */
    platform_ime_data: PlatformImeData  # Data updated by current frame
    # ImGuiPlatformImeData    PlatformImeDataPrev;    /* original C++ signature */
    platform_ime_data_prev: PlatformImeData  # Previous frame data (when changing we will call io.SetPlatformImeDataFn
    # ImGuiID                 PlatformImeViewport;    /* original C++ signature */
    platform_ime_viewport: ID

    # ImGuiDockContext        DockContext;    /* original C++ signature */
    # Extensions
    # FIXME: We could provide an API to register one slot in an array held in ImGuiContext?
    dock_context: DockContext

    # Settings
    # bool                    SettingsLoaded;    /* original C++ signature */
    settings_loaded: bool
    # float                   SettingsDirtyTimer;    /* original C++ signature */
    settings_dirty_timer: float  # Save .ini Settings to memory when time reaches zero
    # ImGuiTextBuffer         SettingsIniData;    /* original C++ signature */
    settings_ini_data: TextBuffer  # In memory .ini settings
    # ImVector<ImGuiSettingsHandler>      SettingsHandlers;    /* original C++ signature */
    settings_handlers: ImVector_SettingsHandler  # List of .ini settings handlers
    # ImGuiID                             HookIdNext;    /* original C++ signature */
    hook_id_next: ID  # Next available HookId

    # Capture/Logging
    # bool                    LogEnabled;    /* original C++ signature */
    log_enabled: bool  # Currently capturing
    # ImGuiLogType            LogType;    /* original C++ signature */
    log_type: LogType  # Capture target
    # ImFileHandle            LogFile;    /* original C++ signature */
    log_file: ImFileHandle  # If != None log to stdout/ file
    # ImGuiTextBuffer         LogBuffer;    /* original C++ signature */
    log_buffer: TextBuffer  # Accumulation buffer when log to clipboard. This is pointer so our GImGui static constructor doesn't call heap allocators.
    # const char*             LogNextPrefix;    /* original C++ signature */
    log_next_prefix: str  # (const)
    # const char*             LogNextSuffix;    /* original C++ signature */
    log_next_suffix: str  # (const)
    # float                   LogLinePosY;    /* original C++ signature */
    log_line_pos_y: float
    # bool                    LogLineFirstItem;    /* original C++ signature */
    log_line_first_item: bool
    # int                     LogDepthRef;    /* original C++ signature */
    log_depth_ref: int
    # int                     LogDepthToExpand;    /* original C++ signature */
    log_depth_to_expand: int
    # int                     LogDepthToExpandDefault;    /* original C++ signature */
    log_depth_to_expand_default: int  # Default/stored value for LogDepthMaxExpand if not specified in the LogXXX function call.

    # Debug Tools
    # ImGuiDebugLogFlags      DebugLogFlags;    /* original C++ signature */
    debug_log_flags: DebugLogFlags
    # ImGuiTextBuffer         DebugLogBuf;    /* original C++ signature */
    debug_log_buf: TextBuffer
    # ImGuiTextIndex          DebugLogIndex;    /* original C++ signature */
    debug_log_index: TextIndex
    # ImU8                    DebugLogClipperAutoDisableFrames;    /* original C++ signature */
    debug_log_clipper_auto_disable_frames: ImU8
    # ImU8                    DebugLocateFrames;    /* original C++ signature */
    debug_locate_frames: ImU8  # For DebugLocateItemOnHover(). This is used together with DebugLocateId which is in a hot/cached spot above.
    # ImS8                    DebugBeginReturnValueCullDepth;    /* original C++ signature */
    debug_begin_return_value_cull_depth: ImS8  # Cycle between 0..9 then wrap around.
    # bool                    DebugItemPickerActive;    /* original C++ signature */
    debug_item_picker_active: bool  # Item picker is active (started with DebugStartItemPicker())
    # ImU8                    DebugItemPickerMouseButton;    /* original C++ signature */
    debug_item_picker_mouse_button: ImU8
    # ImGuiID                 DebugItemPickerBreakId;    /* original C++ signature */
    debug_item_picker_break_id: ID  # Will call IM_DEBUG_BREAK() when encountering this ID
    # ImGuiMetricsConfig      DebugMetricsConfig;    /* original C++ signature */
    debug_metrics_config: MetricsConfig
    # ImGuiIDStackTool        DebugIDStackTool;    /* original C++ signature */
    debug_id_stack_tool: IDStackTool
    # ImGuiDebugAllocInfo     DebugAllocInfo;    /* original C++ signature */
    debug_alloc_info: DebugAllocInfo
    # ImGuiDockNode*          DebugHoveredDockNode;    /* original C++ signature */
    debug_hovered_dock_node: DockNode  # Hovered dock node.

    # Misc
    # float                   FramerateSecPerFrame[60];    /* original C++ signature */
    framerate_sec_per_frame: np.ndarray  # ndarray[type=float, size=60]  # Calculate estimate of framerate for user over the last 60 frames..
    # int                     FramerateSecPerFrameIdx;    /* original C++ signature */
    framerate_sec_per_frame_idx: int
    # int                     FramerateSecPerFrameCount;    /* original C++ signature */
    framerate_sec_per_frame_count: int
    # float                   FramerateSecPerFrameAccum;    /* original C++ signature */
    framerate_sec_per_frame_accum: float
    # int                     WantCaptureMouseNextFrame;    /* original C++ signature */
    want_capture_mouse_next_frame: int  # Explicit capture override via SetNextFrameWantCaptureMouse()/SetNextFrameWantCaptureKeyboard(). Default to -1.
    # int                     WantCaptureKeyboardNextFrame;    /* original C++ signature */
    want_capture_keyboard_next_frame: int  # "
    # int                     WantTextInputNextFrame;    /* original C++ signature */
    want_text_input_next_frame: int
    # ImVector<char>          TempBuffer;    /* original C++ signature */
    temp_buffer: ImVector_char  # Temporary text buffer

    # ImGuiContext(ImFontAtlas* shared_font_atlas)    /* original C++ signature */
    #     {
    #         IO.Ctx = this;
    #         InputTextState.Ctx = this;
    #
    #         Initialized = false;
    #         ConfigFlagsCurrFrame = ConfigFlagsLastFrame = ImGuiConfigFlags_None;
    #         FontAtlasOwnedByContext = shared_font_atlas ? false : true;
    #         Font = NULL;
    #         FontSize = FontBaseSize = 0.0f;
    #         IO.Fonts = shared_font_atlas ? shared_font_atlas : IM_NEW(ImFontAtlas)();
    #         Time = 0.0f;
    #         FrameCount = 0;
    #         FrameCountEnded = FrameCountPlatformEnded = FrameCountRendered = -1;
    #         WithinFrameScope = WithinFrameScopeWithImplicitWindow = WithinEndChild = false;
    #         GcCompactAll = false;
    #         TestEngineHookItems = false;
    #         TestEngine = NULL;
    #
    #         InputEventsNextMouseSource = ImGuiMouseSource_Mouse;
    #         InputEventsNextEventId = 1;
    #
    #         WindowsActiveCount = 0;
    #         CurrentWindow = NULL;
    #         HoveredWindow = NULL;
    #         HoveredWindowUnderMovingWindow = NULL;
    #         MovingWindow = NULL;
    #         WheelingWindow = NULL;
    #         WheelingWindowStartFrame = WheelingWindowScrolledFrame = -1;
    #         WheelingWindowReleaseTimer = 0.0f;
    #
    #         DebugHookIdInfo = 0;
    #         HoveredId = HoveredIdPreviousFrame = 0;
    #         HoveredIdAllowOverlap = false;
    #         HoveredIdDisabled = false;
    #         HoveredIdTimer = HoveredIdNotActiveTimer = 0.0f;
    #         ActiveId = 0;
    #         ActiveIdIsAlive = 0;
    #         ActiveIdTimer = 0.0f;
    #         ActiveIdIsJustActivated = false;
    #         ActiveIdAllowOverlap = false;
    #         ActiveIdNoClearOnFocusLoss = false;
    #         ActiveIdHasBeenPressedBefore = false;
    #         ActiveIdHasBeenEditedBefore = false;
    #         ActiveIdHasBeenEditedThisFrame = false;
    #         ActiveIdClickOffset = ImVec2(-1, -1);
    #         ActiveIdWindow = NULL;
    #         ActiveIdSource = ImGuiInputSource_None;
    #         ActiveIdMouseButton = -1;
    #         ActiveIdPreviousFrame = 0;
    #         ActiveIdPreviousFrameIsAlive = false;
    #         ActiveIdPreviousFrameHasBeenEditedBefore = false;
    #         ActiveIdPreviousFrameWindow = NULL;
    #         LastActiveId = 0;
    #         LastActiveIdTimer = 0.0f;
    #
    #         ActiveIdUsingNavDirMask = 0x00;
    #         ActiveIdUsingAllKeyboardKeys = false;
    #                                                      #ifndef IMGUI_DISABLE_OBSOLETE_KEYIO
    #         ActiveIdUsingNavInputMask = 0x00;
    #                                                      #endif
    #
    #         CurrentFocusScopeId = 0;
    #         CurrentItemFlags = ImGuiItemFlags_None;
    #         DebugShowGroupRects = false;
    #         BeginMenuCount = 0;
    #
    #         CurrentDpiScale = 0.0f;
    #         CurrentViewport = NULL;
    #         MouseViewport = MouseLastHoveredViewport = NULL;
    #         PlatformLastFocusedViewportId = 0;
    #         ViewportCreatedCount = PlatformWindowsCreatedCount = 0;
    #         ViewportFocusedStampCount = 0;
    #
    #         NavWindow = NULL;
    #         NavId = NavFocusScopeId = NavActivateId = NavActivateDownId = NavActivatePressedId = 0;
    #         NavJustMovedToId = NavJustMovedToFocusScopeId = NavNextActivateId = 0;
    #         NavActivateFlags = NavNextActivateFlags = ImGuiActivateFlags_None;
    #         NavJustMovedToKeyMods = ImGuiMod_None;
    #         NavInputSource = ImGuiInputSource_Keyboard;
    #         NavLayer = ImGuiNavLayer_Main;
    #         NavLastValidSelectionUserData = ImGuiSelectionUserData_Invalid;
    #         NavIdIsAlive = false;
    #         NavMousePosDirty = false;
    #         NavDisableHighlight = true;
    #         NavDisableMouseHover = false;
    #         NavAnyRequest = false;
    #         NavInitRequest = false;
    #         NavInitRequestFromMove = false;
    #         NavMoveSubmitted = false;
    #         NavMoveScoringItems = false;
    #         NavMoveForwardToNextFrame = false;
    #         NavMoveFlags = ImGuiNavMoveFlags_None;
    #         NavMoveScrollFlags = ImGuiScrollFlags_None;
    #         NavMoveKeyMods = ImGuiMod_None;
    #         NavMoveDir = NavMoveDirForDebug = NavMoveClipDir = ImGuiDir_None;
    #         NavScoringDebugCount = 0;
    #         NavTabbingDir = 0;
    #         NavTabbingCounter = 0;
    #
    #         ConfigNavWindowingKeyNext = ImGuiMod_Ctrl | ImGuiKey_Tab;
    #         ConfigNavWindowingKeyPrev = ImGuiMod_Ctrl | ImGuiMod_Shift | ImGuiKey_Tab;
    #         NavWindowingTarget = NavWindowingTargetAnim = NavWindowingListWindow = NULL;
    #         NavWindowingTimer = NavWindowingHighlightAlpha = 0.0f;
    #         NavWindowingToggleLayer = false;
    #
    #         DimBgRatio = 0.0f;
    #
    #         DragDropActive = DragDropWithinSource = DragDropWithinTarget = false;
    #         DragDropSourceFlags = ImGuiDragDropFlags_None;
    #         DragDropSourceFrameCount = -1;
    #         DragDropMouseButton = -1;
    #         DragDropTargetId = 0;
    #         DragDropAcceptFlags = ImGuiDragDropFlags_None;
    #         DragDropAcceptIdCurrRectSurface = 0.0f;
    #         DragDropAcceptIdPrev = DragDropAcceptIdCurr = 0;
    #         DragDropAcceptFrameCount = -1;
    #         DragDropHoldJustPressedId = 0;
    #         memset(DragDropPayloadBufLocal, 0, sizeof(DragDropPayloadBufLocal));
    #
    #         ClipperTempDataStacked = 0;
    #
    #         CurrentTable = NULL;
    #         TablesTempDataStacked = 0;
    #         CurrentTabBar = NULL;
    #
    #         HoverItemDelayId = HoverItemDelayIdPreviousFrame = HoverItemUnlockedStationaryId = HoverWindowUnlockedStationaryId = 0;
    #         HoverItemDelayTimer = HoverItemDelayClearTimer = 0.0f;
    #
    #         MouseCursor = ImGuiMouseCursor_Arrow;
    #         MouseStationaryTimer = 0.0f;
    #
    #         TempInputId = 0;
    #         ColorEditOptions = ImGuiColorEditFlags_DefaultOptions_;
    #         ColorEditCurrentID = ColorEditSavedID = 0;
    #         ColorEditSavedHue = ColorEditSavedSat = 0.0f;
    #         ColorEditSavedColor = 0;
    #         WindowResizeRelativeMode = false;
    #         SliderGrabClickOffset = 0.0f;
    #         SliderCurrentAccum = 0.0f;
    #         SliderCurrentAccumDirty = false;
    #         DragCurrentAccumDirty = false;
    #         DragCurrentAccum = 0.0f;
    #         DragSpeedDefaultRatio = 1.0f / 100.0f;
    #         ScrollbarClickDeltaToGrabCenter = 0.0f;
    #         DisabledAlphaBackup = 0.0f;
    #         DisabledStackSize = 0;
    #         LockMarkEdited = 0;
    #         TooltipOverrideCount = 0;
    #
    #         PlatformImeData.InputPos = ImVec2(0.0f, 0.0f);
    #         PlatformImeDataPrev.InputPos = ImVec2(-1.0f, -1.0f); // Different to ensure initial submission
    #         PlatformImeViewport = 0;
    #
    #         DockNodeWindowMenuHandler = NULL;
    #
    #         SettingsLoaded = false;
    #         SettingsDirtyTimer = 0.0f;
    #         HookIdNext = 0;
    #
    #         memset(LocalizationTable, 0, sizeof(LocalizationTable));
    #
    #         LogEnabled = false;
    #         LogType = ImGuiLogType_None;
    #         LogNextPrefix = LogNextSuffix = NULL;
    #         LogFile = NULL;
    #         LogLinePosY = FLT_MAX;
    #         LogLineFirstItem = false;
    #         LogDepthRef = 0;
    #         LogDepthToExpand = LogDepthToExpandDefault = 2;
    #
    #         DebugLogFlags = ImGuiDebugLogFlags_OutputToTTY;
    #         DebugLocateId = 0;
    #         DebugLogClipperAutoDisableFrames = 0;
    #         DebugLocateFrames = 0;
    #         DebugBeginReturnValueCullDepth = -1;
    #         DebugItemPickerActive = false;
    #         DebugItemPickerMouseButton = ImGuiMouseButton_Left;
    #         DebugItemPickerBreakId = 0;
    #         DebugHoveredDockNode = NULL;
    #
    #         memset(FramerateSecPerFrame, 0, sizeof(FramerateSecPerFrame));
    #         FramerateSecPerFrameIdx = FramerateSecPerFrameCount = 0;
    #         FramerateSecPerFrameAccum = 0.0f;
    #         WantCaptureMouseNextFrame = WantCaptureKeyboardNextFrame = WantTextInputNextFrame = -1;
    #     }
    def __init__(self, shared_font_atlas: ImFontAtlas) -> None:
        pass

# -----------------------------------------------------------------------------
# [SECTION] ImGuiWindowTempData, ImGuiWindow
# -----------------------------------------------------------------------------

class WindowTempData:
    """Transient per-window data, reset at the beginning of the frame. This used to be called ImGuiDrawContext, hence the DC variable name in ImGuiWindow.
    (That's theory, in practice the delimitation between ImGuiWindow and ImGuiWindowTempData is quite tenuous and could be reconsidered..)
    (This doesn't need a constructor because we zero-clear it as part of ImGuiWindow and all frame-temporary data are setup on Begin)
    """

    # Layout
    # ImVec2                  CursorPos;    /* original C++ signature */
    cursor_pos: ImVec2  # Current emitting position, in absolute coordinates.
    # ImVec2                  CursorPosPrevLine;    /* original C++ signature */
    cursor_pos_prev_line: ImVec2
    # ImVec2                  CursorStartPos;    /* original C++ signature */
    cursor_start_pos: ImVec2  # Initial position after Begin(), generally ~ window position + WindowPadding.
    # ImVec2                  CursorMaxPos;    /* original C++ signature */
    cursor_max_pos: ImVec2  # Used to implicitly calculate ContentSize at the beginning of next frame, for scrolling range and auto-resize. Always growing during the frame.
    # ImVec2                  IdealMaxPos;    /* original C++ signature */
    ideal_max_pos: ImVec2  # Used to implicitly calculate ContentSizeIdeal at the beginning of next frame, for auto-resize only. Always growing during the frame.
    # ImVec2                  CurrLineSize;    /* original C++ signature */
    curr_line_size: ImVec2
    # ImVec2                  PrevLineSize;    /* original C++ signature */
    prev_line_size: ImVec2
    # float                   CurrLineTextBaseOffset;    /* original C++ signature */
    curr_line_text_base_offset: float  # Baseline offset (0.0 by default on a new line, generally == style.FramePadding.y when a framed item has been added).
    # float                   PrevLineTextBaseOffset;    /* original C++ signature */
    prev_line_text_base_offset: float
    # bool                    IsSameLine;    /* original C++ signature */
    is_same_line: bool
    # bool                    IsSetPos;    /* original C++ signature */
    is_set_pos: bool
    # ImVec1                  Indent;    /* original C++ signature */
    indent: ImVec1  # Indentation / start position from left of window (increased by TreePush/TreePop, etc.)
    # ImVec1                  ColumnsOffset;    /* original C++ signature */
    columns_offset: ImVec1  # Offset to the current column (if ColumnsCurrent > 0). FIXME: This and the above should be a stack to allow use cases like Tree->Column->Tree. Need revamp columns API.
    # ImVec1                  GroupOffset;    /* original C++ signature */
    group_offset: ImVec1
    # ImVec2                  CursorStartPosLossyness;    /* original C++ signature */
    cursor_start_pos_lossyness: ImVec2  # Record the loss of precision of CursorStartPos due to really large scrolling amount. This is used by clipper to compensate and fix the most common use case of large scroll area.

    # Keyboard/Gamepad navigation
    # ImGuiNavLayer           NavLayerCurrent;    /* original C++ signature */
    nav_layer_current: NavLayer  # Current layer, 0..31 (we currently only use 0..1)
    # short                   NavLayersActiveMask;    /* original C++ signature */
    nav_layers_active_mask: int  # Which layers have been written to (result from previous frame)
    # short                   NavLayersActiveMaskNext;    /* original C++ signature */
    nav_layers_active_mask_next: int  # Which layers have been written to (accumulator for current frame)
    # bool                    NavIsScrollPushableX;    /* original C++ signature */
    nav_is_scroll_pushable_x: bool  # Set when current work location may be scrolled horizontally when moving left / right. This is generally always True UNLESS within a column.
    # bool                    NavHideHighlightOneFrame;    /* original C++ signature */
    nav_hide_highlight_one_frame: bool
    # bool                    NavWindowHasScrollY;    /* original C++ signature */
    nav_window_has_scroll_y: bool  # Set per window when scrolling can be used (== ScrollMax.y > 0.0)

    # Miscellaneous
    # bool                    MenuBarAppending;    /* original C++ signature */
    menu_bar_appending: bool  # FIXME: Remove this
    # ImVec2                  MenuBarOffset;    /* original C++ signature */
    menu_bar_offset: ImVec2  # MenuBarOffset.x is sort of equivalent of a per-layer CursorPos.x, saved/restored as we switch to the menu bar. The only situation when MenuBarOffset.y is > 0 if when (SafeAreaPadding.y > FramePadding.y), often used on TVs.
    # ImGuiMenuColumns        MenuColumns;    /* original C++ signature */
    menu_columns: MenuColumns  # Simplified columns storage for menu items measurement
    # int                     TreeDepth;    /* original C++ signature */
    tree_depth: int  # Current tree depth.
    # ImU32                   TreeJumpToParentOnPopMask;    /* original C++ signature */
    tree_jump_to_parent_on_pop_mask: ImU32  # Store a copy of !g.NavIdIsAlive for TreeDepth 0..31.. Could be turned into a ImU64 if necessary.
    # ImVector<ImGuiWindow*>  ChildWindows;    /* original C++ signature */
    child_windows: ImVector_Window_ptr
    # ImGuiStorage*           StateStorage;    /* original C++ signature */
    state_storage: Storage  # Current persistent per-window storage (store e.g. tree node open/close state)
    # ImGuiOldColumns*        CurrentColumns;    /* original C++ signature */
    current_columns: OldColumns  # Current columns set
    # int                     CurrentTableIdx;    /* original C++ signature */
    current_table_idx: int  # Current table index (into g.Tables)
    # ImGuiLayoutType         LayoutType;    /* original C++ signature */
    layout_type: LayoutType
    # ImGuiLayoutType         ParentLayoutType;    /* original C++ signature */
    parent_layout_type: LayoutType  # Layout type of parent window at the time of Begin()

    # Local parameters stacks
    # We store the current settings outside of the vectors to increase memory locality (reduce cache misses). The vectors are rarely modified. Also it allows us to not heap allocate for short-lived windows which are not using those settings.
    # float                   ItemWidth;    /* original C++ signature */
    item_width: float  # Current item width (>0.0: width in pixels, <0.0: align xx pixels to the right of window).
    # float                   TextWrapPos;    /* original C++ signature */
    text_wrap_pos: float  # Current text wrap pos.
    # ImVector<float>         ItemWidthStack;    /* original C++ signature */
    item_width_stack: ImVector_float  # Store item widths to restore (attention: .back() is not == ItemWidth)
    # ImVector<float>         TextWrapPosStack;    /* original C++ signature */
    text_wrap_pos_stack: ImVector_float  # Store text wrap pos to restore (attention: .back() is not == TextWrapPos)
    # ImGuiWindowTempData(ImVec2 CursorPos = ImVec2(), ImVec2 CursorPosPrevLine = ImVec2(), ImVec2 CursorStartPos = ImVec2(), ImVec2 CursorMaxPos = ImVec2(), ImVec2 IdealMaxPos = ImVec2(), ImVec2 CurrLineSize = ImVec2(), ImVec2 PrevLineSize = ImVec2(), float CurrLineTextBaseOffset = float(), float PrevLineTextBaseOffset = float(), bool IsSameLine = bool(), bool IsSetPos = bool(), ImVec1 Indent = ImVec1(), ImVec1 ColumnsOffset = ImVec1(), ImVec1 GroupOffset = ImVec1(), ImVec2 CursorStartPosLossyness = ImVec2(), ImGuiNavLayer NavLayerCurrent = ImGuiNavLayer(), short NavLayersActiveMask = short(), short NavLayersActiveMaskNext = short(), bool NavIsScrollPushableX = bool(), bool NavHideHighlightOneFrame = bool(), bool NavWindowHasScrollY = bool(), bool MenuBarAppending = bool(), ImVec2 MenuBarOffset = ImVec2(), ImGuiMenuColumns MenuColumns = ImGuiMenuColumns(), int TreeDepth = int(), ImU32 TreeJumpToParentOnPopMask = ImU32(), ImVector<ImGuiWindow*> ChildWindows = ImVector<ImGuiWindow*>(), int CurrentTableIdx = int(), ImGuiLayoutType LayoutType = ImGuiLayoutType(), ImGuiLayoutType ParentLayoutType = ImGuiLayoutType(), float ItemWidth = float(), float TextWrapPos = float(), ImVector<float> ItemWidthStack = ImVector<float>(), ImVector<float> TextWrapPosStack = ImVector<float>());    /* original C++ signature */
    def __init__(
        self,
        cursor_pos: ImVec2 = ImVec2(),
        cursor_pos_prev_line: ImVec2 = ImVec2(),
        cursor_start_pos: ImVec2 = ImVec2(),
        cursor_max_pos: ImVec2 = ImVec2(),
        ideal_max_pos: ImVec2 = ImVec2(),
        curr_line_size: ImVec2 = ImVec2(),
        prev_line_size: ImVec2 = ImVec2(),
        curr_line_text_base_offset: float = float(),
        prev_line_text_base_offset: float = float(),
        is_same_line: bool = bool(),
        is_set_pos: bool = bool(),
        indent: ImVec1 = ImVec1(),
        columns_offset: ImVec1 = ImVec1(),
        group_offset: ImVec1 = ImVec1(),
        cursor_start_pos_lossyness: ImVec2 = ImVec2(),
        nav_layer_current: NavLayer = NavLayer(),
        nav_layers_active_mask: int = int(),
        nav_layers_active_mask_next: int = int(),
        nav_is_scroll_pushable_x: bool = bool(),
        nav_hide_highlight_one_frame: bool = bool(),
        nav_window_has_scroll_y: bool = bool(),
        menu_bar_appending: bool = bool(),
        menu_bar_offset: ImVec2 = ImVec2(),
        menu_columns: MenuColumns = MenuColumns(),
        tree_depth: int = int(),
        tree_jump_to_parent_on_pop_mask: ImU32 = ImU32(),
        child_windows: ImVector_Window_ptr = ImVector_Window_ptr(),
        current_table_idx: int = int(),
        layout_type: LayoutType = LayoutType(),
        parent_layout_type: LayoutType = LayoutType(),
        item_width: float = float(),
        text_wrap_pos: float = float(),
        item_width_stack: ImVector_float = ImVector_float(),
        text_wrap_pos_stack: ImVector_float = ImVector_float(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class Window:
    """Storage for one window"""

    # ImGuiContext*           Ctx;    /* original C++ signature */
    ctx: Context  # Parent UI context (needs to be set explicitly by parent).
    # char*                   Name;    /* original C++ signature */
    name: char  # Window name, owned by the window. # (read-only)
    # ImGuiID                 ID;    /* original C++ signature */
    id_: ID  # == ImHashStr(Name)
    # ImGuiWindowFlags        Flags,     /* original C++ signature */
    flags: WindowFlags  # See enum ImGuiWindowFlags_
    # FlagsPreviousFrame;    /* original C++ signature */
    flags_previous_frame: WindowFlags  # See enum ImGuiWindowFlags_
    # ImGuiChildFlags         ChildFlags;    /* original C++ signature */
    child_flags: ChildFlags  # Set when window is a child window. See enum ImGuiChildFlags_
    # ImGuiWindowClass        WindowClass;    /* original C++ signature */
    window_class: WindowClass  # Advanced users only. Set with SetNextWindowClass()
    # ImGuiViewportP*         Viewport;    /* original C++ signature */
    viewport: ViewportP  # Always set in Begin(). Inactive windows may have a None value here if their viewport was discarded.
    # ImGuiID                 ViewportId;    /* original C++ signature */
    viewport_id: ID  # We backup the viewport id (since the viewport may disappear or never be created if the window is inactive)
    # ImVec2                  ViewportPos;    /* original C++ signature */
    viewport_pos: ImVec2  # We backup the viewport position (since the viewport may disappear or never be created if the window is inactive)
    # int                     ViewportAllowPlatformMonitorExtend;    /* original C++ signature */
    viewport_allow_platform_monitor_extend: int  # Reset to -1 every frame (index is guaranteed to be valid between NewFrame..EndFrame), only used in the Appearing frame of a tooltip/popup to enforce clamping to a given monitor
    # ImVec2                  Pos;    /* original C++ signature */
    pos: ImVec2  # Position (always rounded-up to nearest pixel)
    # ImVec2                  Size;    /* original C++ signature */
    size: ImVec2  # Current size (==SizeFull or collapsed title bar size)
    # ImVec2                  SizeFull;    /* original C++ signature */
    size_full: ImVec2  # Size when non collapsed
    # ImVec2                  ContentSize;    /* original C++ signature */
    content_size: ImVec2  # Size of contents/scrollable client area (calculated from the extents reach of the cursor) from previous frame. Does not include window decoration or window padding.
    # ImVec2                  ContentSizeIdeal;    /* original C++ signature */
    content_size_ideal: ImVec2
    # ImVec2                  ContentSizeExplicit;    /* original C++ signature */
    content_size_explicit: ImVec2  # Size of contents/scrollable client area explicitly request by the user via SetNextWindowContentSize().
    # ImVec2                  WindowPadding;    /* original C++ signature */
    window_padding: ImVec2  # Window padding at the time of Begin().
    # float                   WindowRounding;    /* original C++ signature */
    window_rounding: float  # Window rounding at the time of Begin(). May be clamped lower to avoid rendering artifacts with title bar, menu bar etc.
    # float                   WindowBorderSize;    /* original C++ signature */
    window_border_size: float  # Window border size at the time of Begin().
    # float                   DecoOuterSizeX1,     /* original C++ signature */
    deco_outer_size_x1: float  # Left/Up offsets. Sum of non-scrolling outer decorations (X1 generally == 0.0. Y1 generally = TitleBarHeight + MenuBarHeight). Locked during Begin().
    # DecoOuterSizeY1;    /* original C++ signature */
    deco_outer_size_y1: float  # Left/Up offsets. Sum of non-scrolling outer decorations (X1 generally == 0.0. Y1 generally = TitleBarHeight + MenuBarHeight). Locked during Begin().
    # float                   DecoOuterSizeX2,     /* original C++ signature */
    deco_outer_size_x2: float  # Right/Down offsets (X2 generally == ScrollbarSize.x, Y2 == ScrollbarSizes.y).
    # DecoOuterSizeY2;    /* original C++ signature */
    deco_outer_size_y2: float  # Right/Down offsets (X2 generally == ScrollbarSize.x, Y2 == ScrollbarSizes.y).
    # float                   DecoInnerSizeX1,     /* original C++ signature */
    deco_inner_size_x1: float  # Applied AFTER/OVER InnerRect. Specialized for Tables as they use specialized form of clipping and frozen rows/columns are inside InnerRect (and not part of regular decoration sizes).
    # DecoInnerSizeY1;    /* original C++ signature */
    deco_inner_size_y1: float  # Applied AFTER/OVER InnerRect. Specialized for Tables as they use specialized form of clipping and frozen rows/columns are inside InnerRect (and not part of regular decoration sizes).
    # int                     NameBufLen;    /* original C++ signature */
    name_buf_len: int  # Size of buffer storing Name. May be larger than strlen(Name)!
    # ImGuiID                 MoveId;    /* original C++ signature */
    move_id: ID  # == window->GetID("#MOVE")
    # ImGuiID                 TabId;    /* original C++ signature */
    tab_id: ID  # == window->GetID("#TAB")
    # ImGuiID                 ChildId;    /* original C++ signature */
    child_id: ID  # ID of corresponding item in parent window (for navigation to return from child window to parent window)
    # ImVec2                  Scroll;    /* original C++ signature */
    scroll: ImVec2
    # ImVec2                  ScrollMax;    /* original C++ signature */
    scroll_max: ImVec2
    # ImVec2                  ScrollTarget;    /* original C++ signature */
    scroll_target: ImVec2  # target scroll position. stored as cursor position with scrolling canceled out, so the highest point is always 0.0. (FLT_MAX for no change)
    # ImVec2                  ScrollTargetCenterRatio;    /* original C++ signature */
    scroll_target_center_ratio: ImVec2  # 0.0 = scroll so that target position is at top, 0.5 = scroll so that target position is centered
    # ImVec2                  ScrollTargetEdgeSnapDist;    /* original C++ signature */
    scroll_target_edge_snap_dist: ImVec2  # 0.0 = no snapping, >0.0 snapping threshold
    # ImVec2                  ScrollbarSizes;    /* original C++ signature */
    scrollbar_sizes: ImVec2  # Size taken by each scrollbars on their smaller axis. Pay attention! ScrollbarSizes.x == width of the vertical scrollbar, ScrollbarSizes.y = height of the horizontal scrollbar.
    # bool                    ScrollbarX,     /* original C++ signature */
    scrollbar_x: bool  # Are scrollbars visible?
    # ScrollbarY;    /* original C++ signature */
    scrollbar_y: bool  # Are scrollbars visible?
    # bool                    ViewportOwned;    /* original C++ signature */
    viewport_owned: bool
    # bool                    Active;    /* original C++ signature */
    active: bool  # Set to True on Begin(), unless Collapsed
    # bool                    WasActive;    /* original C++ signature */
    was_active: bool
    # bool                    WriteAccessed;    /* original C++ signature */
    write_accessed: bool  # Set to True when any widget access the current window
    # bool                    Collapsed;    /* original C++ signature */
    collapsed: bool  # Set when collapsing window to become only title-bar
    # bool                    WantCollapseToggle;    /* original C++ signature */
    want_collapse_toggle: bool
    # bool                    SkipItems;    /* original C++ signature */
    skip_items: bool  # Set when items can safely be all clipped (e.g. window not visible or collapsed)
    # bool                    Appearing;    /* original C++ signature */
    appearing: bool  # Set during the frame where the window is appearing (or re-appearing)
    # bool                    Hidden;    /* original C++ signature */
    hidden: bool  # Do not display (== HiddenFrames*** > 0)
    # bool                    IsFallbackWindow;    /* original C++ signature */
    is_fallback_window: bool  # Set on the "Debug##Default" window.
    # bool                    IsExplicitChild;    /* original C++ signature */
    is_explicit_child: bool  # Set when passed _ChildWindow, left to False by BeginDocked()
    # bool                    HasCloseButton;    /* original C++ signature */
    has_close_button: bool  # Set when the window has a close button (p_open != None)
    # signed char             ResizeBorderHovered;    /* original C++ signature */
    resize_border_hovered: int  # Current border being hovered for resize (-1: none, otherwise 0-3)
    # signed char             ResizeBorderHeld;    /* original C++ signature */
    resize_border_held: int  # Current border being held for resize (-1: none, otherwise 0-3)
    # short                   BeginCount;    /* original C++ signature */
    begin_count: int  # Number of Begin() during the current frame (generally 0 or 1, 1+ if appending via multiple Begin/End pairs)
    # short                   BeginCountPreviousFrame;    /* original C++ signature */
    begin_count_previous_frame: int  # Number of Begin() during the previous frame
    # short                   BeginOrderWithinParent;    /* original C++ signature */
    begin_order_within_parent: int  # Begin() order within immediate parent window, if we are a child window. Otherwise 0.
    # short                   BeginOrderWithinContext;    /* original C++ signature */
    begin_order_within_context: int  # Begin() order within entire imgui context. This is mostly used for debugging submission order related issues.
    # short                   FocusOrder;    /* original C++ signature */
    focus_order: int  # Order within WindowsFocusOrder[], altered when windows are focused.
    # ImGuiID                 PopupId;    /* original C++ signature */
    popup_id: ID  # ID in the popup stack when this window is used as a popup/menu (because we use generic Name/ID for recycling)
    # ImS8                    AutoFitFramesX,     /* original C++ signature */
    auto_fit_frames_x: ImS8
    # AutoFitFramesY;    /* original C++ signature */
    auto_fit_frames_y: ImS8
    # bool                    AutoFitOnlyGrows;    /* original C++ signature */
    auto_fit_only_grows: bool
    # ImGuiDir                AutoPosLastDirection;    /* original C++ signature */
    auto_pos_last_direction: Dir
    # ImS8                    HiddenFramesCanSkipItems;    /* original C++ signature */
    hidden_frames_can_skip_items: ImS8  # Hide the window for N frames
    # ImS8                    HiddenFramesCannotSkipItems;    /* original C++ signature */
    hidden_frames_cannot_skip_items: ImS8  # Hide the window for N frames while allowing items to be submitted so we can measure their size
    # ImS8                    HiddenFramesForRenderOnly;    /* original C++ signature */
    hidden_frames_for_render_only: ImS8  # Hide the window until frame N at Render() time only
    # ImS8                    DisableInputsFrames;    /* original C++ signature */
    disable_inputs_frames: ImS8  # Disable window interactions for N frames
    # ImVec2                  SetWindowPosVal;    /* original C++ signature */
    set_window_pos_val: ImVec2  # store window position when using a non-zero Pivot (position set needs to be processed when we know the window size)
    # ImVec2                  SetWindowPosPivot;    /* original C++ signature */
    set_window_pos_pivot: ImVec2  # store window pivot for positioning. ImVec2(0, 0) when positioning from top-left corner; ImVec2(0.5, 0.5) for centering; ImVec2(1, 1) for bottom right.

    # ImVector<ImGuiID>       IDStack;    /* original C++ signature */
    id_stack: ImVector_ID  # ID stack. ID are hashes seeded with the value at the top of the stack. (In theory this should be in the TempData structure)
    # ImGuiWindowTempData     DC;    /* original C++ signature */
    dc: WindowTempData  # Temporary per-window data, reset at the beginning of the frame. This used to be called ImGuiDrawContext, hence the "DC" variable name.

    # The best way to understand what those rectangles are is to use the 'Metrics->Tools->Show Windows Rectangles' viewer.
    # The main 'OuterRect', omitted as a field, is window->Rect().
    # ImRect                  OuterRectClipped;    /* original C++ signature */
    outer_rect_clipped: ImRect  # == Window->Rect() just after setup in Begin(). == window->Rect() for root window.
    # ImRect                  InnerRect;    /* original C++ signature */
    inner_rect: ImRect  # Inner rectangle (omit title bar, menu bar, scroll bar)
    # ImRect                  InnerClipRect;    /* original C++ signature */
    inner_clip_rect: ImRect  # == InnerRect shrunk by WindowPadding*0.5 on each side, clipped within viewport or parent clip rect.
    # ImRect                  WorkRect;    /* original C++ signature */
    work_rect: ImRect  # Initially covers the whole scrolling region. Reduced by containers e.g columns/tables when active. Shrunk by WindowPadding*1.0 on each side. This is meant to replace ContentRegionRect over time (from 1.71+ onward).
    # ImRect                  ParentWorkRect;    /* original C++ signature */
    parent_work_rect: ImRect  # Backup of WorkRect before entering a container such as columns/tables. Used by e.g. SpanAllColumns functions to easily access. Stacked containers are responsible for maintaining this. // FIXME-WORKRECT: Could be a stack?
    # ImRect                  ClipRect;    /* original C++ signature */
    clip_rect: ImRect  # Current clipping/scissoring rectangle, evolve as we are using PushClipRect(), etc. == DrawList->clip_rect_stack.back().
    # ImRect                  ContentRegionRect;    /* original C++ signature */
    content_region_rect: ImRect  # FIXME: This is currently confusing/misleading. It is essentially WorkRect but not handling of scrolling. We currently rely on it as right/bottom aligned sizing operation need some size to rely on.
    # ImVec2ih                HitTestHoleSize;    /* original C++ signature */
    hit_test_hole_size: ImVec2ih  # Define an optional rectangular hole where mouse will pass-through the window.
    # ImVec2ih                HitTestHoleOffset;    /* original C++ signature */
    hit_test_hole_offset: ImVec2ih

    # int                     LastFrameActive;    /* original C++ signature */
    last_frame_active: int  # Last frame number the window was Active.
    # int                     LastFrameJustFocused;    /* original C++ signature */
    last_frame_just_focused: int  # Last frame number the window was made Focused.
    # float                   LastTimeActive;    /* original C++ signature */
    last_time_active: float  # Last timestamp the window was Active (using float as we don't need high precision there)
    # float                   ItemWidthDefault;    /* original C++ signature */
    item_width_default: float
    # ImGuiStorage            StateStorage;    /* original C++ signature */
    state_storage: Storage
    # ImVector<ImGuiOldColumns> ColumnsStorage;    /* original C++ signature */
    columns_storage: ImVector_OldColumns
    # float                   FontWindowScale;    /* original C++ signature */
    font_window_scale: float  # User scale multiplier per-window, via SetWindowFontScale()
    # float                   FontDpiScale;    /* original C++ signature */
    font_dpi_scale: float
    # int                     SettingsOffset;    /* original C++ signature */
    settings_offset: int  # Offset into SettingsWindows[] (offsets are always valid as we only grow the array from the back)

    # ImDrawList*             DrawList;    /* original C++ signature */
    draw_list: ImDrawList  # == &DrawListInst (for backward compatibility reason with code using imgui_internal.h we keep this a pointer)
    # ImDrawList              DrawListInst;    /* original C++ signature */
    draw_list_inst: ImDrawList
    # ImGuiWindow*            ParentWindow;    /* original C++ signature */
    parent_window: Window  # If we are a child _or_ popup _or_ docked window, this is pointing to our parent. Otherwise None.
    # ImGuiWindow*            ParentWindowInBeginStack;    /* original C++ signature */
    parent_window_in_begin_stack: Window
    # ImGuiWindow*            RootWindow;    /* original C++ signature */
    root_window: Window  # Point to ourself or first ancestor that is not a child window. Doesn't cross through popups/dock nodes.
    # ImGuiWindow*            RootWindowPopupTree;    /* original C++ signature */
    root_window_popup_tree: Window  # Point to ourself or first ancestor that is not a child window. Cross through popups parent<>child.
    # ImGuiWindow*            RootWindowDockTree;    /* original C++ signature */
    root_window_dock_tree: Window  # Point to ourself or first ancestor that is not a child window. Cross through dock nodes.
    # ImGuiWindow*            RootWindowForTitleBarHighlight;    /* original C++ signature */
    root_window_for_title_bar_highlight: Window  # Point to ourself or first ancestor which will display TitleBgActive color when this window is active.
    # ImGuiWindow*            RootWindowForNav;    /* original C++ signature */
    root_window_for_nav: Window  # Point to ourself or first ancestor which doesn't have the NavFlattened flag.

    # ImGuiWindow*            NavLastChildNavWindow;    /* original C++ signature */
    nav_last_child_nav_window: Window  # When going to the menu bar, we remember the child window we came from. (This could probably be made implicit if we kept g.Windows sorted by last focused including child window.)
    # ImGuiID                 NavRootFocusScopeId;    /* original C++ signature */
    nav_root_focus_scope_id: ID  # Focus Scope ID at the time of Begin()

    # int                     MemoryDrawListIdxCapacity;    /* original C++ signature */
    memory_draw_list_idx_capacity: int  # Backup of last idx/vtx count, so when waking up the window we can preallocate and avoid iterative alloc/copy
    # int                     MemoryDrawListVtxCapacity;    /* original C++ signature */
    memory_draw_list_vtx_capacity: int
    # bool                    MemoryCompacted;    /* original C++ signature */
    memory_compacted: bool  # Set when window extraneous data have been garbage collected

    # Docking
    # short                   DockOrder;    /* original C++ signature */
    dock_order: int  # Order of the last time the window was visible within its DockNode. This is used to reorder windows that are reappearing on the same frame. Same value between windows that were active and windows that were none are possible.
    # ImGuiWindowDockStyle    DockStyle;    /* original C++ signature */
    dock_style: WindowDockStyle
    # ImGuiDockNode*          DockNode;    /* original C++ signature */
    dock_node: DockNode  # Which node are we docked into. Important: Prefer testing DockIsActive in many cases as this will still be set when the dock node is hidden.
    # ImGuiDockNode*          DockNodeAsHost;    /* original C++ signature */
    dock_node_as_host: DockNode  # Which node are we owning (for parent windows)
    # ImGuiID                 DockId;    /* original C++ signature */
    dock_id: ID  # Backup of last valid DockNode->ID, so single window remember their dock node id even when they are not bound any more
    # ImGuiItemStatusFlags    DockTabItemStatusFlags;    /* original C++ signature */
    dock_tab_item_status_flags: ItemStatusFlags
    # ImRect                  DockTabItemRect;    /* original C++ signature */
    dock_tab_item_rect: ImRect

    # ImGuiWindow(ImGuiContext* context, const char* name);    /* original C++ signature */
    def __init__(self, context: Context, name: str) -> None:
        pass
    # ImGuiID     GetID(const char* str, const char* str_end = NULL);    /* original C++ signature */
    @overload
    def get_id(self, str: str, str_end: Optional[str] = None) -> ID:
        """(private API)"""
        pass
    # ImGuiID     GetID(const void* ptr);    /* original C++ signature */
    @overload
    def get_id(self, ptr: Any) -> ID:
        """(private API)"""
        pass
    # ImGuiID     GetID(int n);    /* original C++ signature */
    @overload
    def get_id(self, n: int) -> ID:
        """(private API)"""
        pass
    # ImGuiID     GetIDFromRectangle(const ImRect& r_abs);    /* original C++ signature */
    def get_id_from_rectangle(self, r_abs: ImRect) -> ID:
        """(private API)"""
        pass
    # We don't use g.FontSize because the window may be != g.CurrentWindow.
    # ImRect      Rect() const            { return ImRect(Pos.x, Pos.y, Pos.x + Size.x, Pos.y + Size.y); }    /* original C++ signature */
    def rect(self) -> ImRect:
        """(private API)"""
        pass
    # float       CalcFontSize() const    { ImGuiContext& g = *Ctx; float scale = g.FontBaseSize * FontWindowScale * FontDpiScale; if (ParentWindow) scale *= ParentWindow->FontWindowScale; return scale; }    /* original C++ signature */
    def calc_font_size(self) -> float:
        """(private API)"""
        pass
    # float       TitleBarHeight() const  { ImGuiContext& g = *Ctx; return (Flags & ImGuiWindowFlags_NoTitleBar) ? 0.0f : CalcFontSize() + g.Style.FramePadding.y * 2.0f; }    /* original C++ signature */
    def title_bar_height(self) -> float:
        """(private API)"""
        pass
    # ImRect      TitleBarRect() const    { return ImRect(Pos, ImVec2(Pos.x + SizeFull.x, Pos.y + TitleBarHeight())); }    /* original C++ signature */
    def title_bar_rect(self) -> ImRect:
        """(private API)"""
        pass
    # float       MenuBarHeight() const   { ImGuiContext& g = *Ctx; return (Flags & ImGuiWindowFlags_MenuBar) ? DC.MenuBarOffset.y + CalcFontSize() + g.Style.FramePadding.y * 2.0f : 0.0f; }    /* original C++ signature */
    def menu_bar_height(self) -> float:
        """(private API)"""
        pass
    # ImRect      MenuBarRect() const     { float y1 = Pos.y + TitleBarHeight(); return ImRect(Pos.x, y1, Pos.x + SizeFull.x, y1 + MenuBarHeight()); }    /* original C++ signature */
    def menu_bar_rect(self) -> ImRect:
        """(private API)"""
        pass

# -----------------------------------------------------------------------------
# [SECTION] Tab bar, Tab item support
# -----------------------------------------------------------------------------

class TabBarFlagsPrivate_(enum.Enum):
    """Extend ImGuiTabBarFlags_"""

    # ImGuiTabBarFlags_DockNode                   = 1 << 20,      /* original C++ signature */
    im_gui_tab_bar_flags_dock_node = (
        enum.auto()
    )  # (= 1 << 20)  # Part of a dock node [we don't use this in the master branch but it facilitate branch syncing to keep this around]
    # ImGuiTabBarFlags_IsFocused                  = 1 << 21,    /* original C++ signature */
    im_gui_tab_bar_flags_is_focused = enum.auto()  # (= 1 << 21)
    # ImGuiTabBarFlags_SaveSettings               = 1 << 22,      /* original C++ signature */
    im_gui_tab_bar_flags_save_settings = (
        enum.auto()
    )  # (= 1 << 22)  # FIXME: Settings are handled by the docking system, this only request the tab bar to mark settings dirty when reordering tabs

class TabItemFlagsPrivate_(enum.Enum):
    """Extend ImGuiTabItemFlags_"""

    # ImGuiTabItemFlags_SectionMask_              = ImGuiTabItemFlags_Leading | ImGuiTabItemFlags_Trailing,    /* original C++ signature */
    im_gui_tab_item_flags_section_mask_ = (
        enum.auto()
    )  # (= TabItemFlags_Leading | TabItemFlags_Trailing)
    # ImGuiTabItemFlags_NoCloseButton             = 1 << 20,      /* original C++ signature */
    im_gui_tab_item_flags_no_close_button = (
        enum.auto()
    )  # (= 1 << 20)  # Track whether p_open was set or not (we'll need this info on the next frame to recompute ContentWidth during layout)
    # ImGuiTabItemFlags_Button                    = 1 << 21,      /* original C++ signature */
    im_gui_tab_item_flags_button = (
        enum.auto()
    )  # (= 1 << 21)  # Used by TabItemButton, change the tab item behavior to mimic a button
    # ImGuiTabItemFlags_Unsorted                  = 1 << 22,      /* original C++ signature */
    im_gui_tab_item_flags_unsorted = (
        enum.auto()
    )  # (= 1 << 22)  # [Docking] Trailing tabs with the _Unsorted flag will be sorted based on the DockOrder of their Window.

class TabItem:
    """Storage for one active tab item (sizeof() 48 bytes)"""

    # ImGuiID             ID;    /* original C++ signature */
    id_: ID
    # ImGuiTabItemFlags   Flags;    /* original C++ signature */
    flags: TabItemFlags
    # ImGuiWindow*        Window;    /* original C++ signature */
    window: Window  # When TabItem is part of a DockNode's TabBar, we hold on to a window.
    # int                 LastFrameVisible;    /* original C++ signature */
    last_frame_visible: int
    # int                 LastFrameSelected;    /* original C++ signature */
    last_frame_selected: int  # This allows us to infer an ordered list of the last activated tabs with little maintenance
    # float               Offset;    /* original C++ signature */
    offset: float  # Position relative to beginning of tab
    # float               Width;    /* original C++ signature */
    width: float  # Width currently displayed
    # float               ContentWidth;    /* original C++ signature */
    content_width: float  # Width of label, stored during BeginTabItem() call
    # float               RequestedWidth;    /* original C++ signature */
    requested_width: float  # Width optionally requested by caller, -1.0 is unused
    # ImS32               NameOffset;    /* original C++ signature */
    name_offset: ImS32  # When Window==None, offset to name within parent ImGuiTabBar::TabsNames
    # ImS16               BeginOrder;    /* original C++ signature */
    begin_order: ImS16  # BeginTabItem() order, used to re-order tabs after toggling ImGuiTabBarFlags_Reorderable
    # ImS16               IndexDuringLayout;    /* original C++ signature */
    index_during_layout: ImS16  # Index only used during TabBarLayout(). Tabs gets reordered so 'Tabs[n].IndexDuringLayout == n' but may mismatch during additions.
    # bool                WantClose;    /* original C++ signature */
    want_close: bool  # Marked as closed by SetTabItemClosed()

    # ImGuiTabItem()      { memset(this, 0, sizeof(*this)); LastFrameVisible = LastFrameSelected = -1; RequestedWidth = -1.0f; NameOffset = -1; BeginOrder = IndexDuringLayout = -1; }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class TabBar:
    """Storage for a tab bar (sizeof() 152 bytes)"""

    # ImVector<ImGuiTabItem> Tabs;    /* original C++ signature */
    tabs: ImVector_TabItem
    # ImGuiTabBarFlags    Flags;    /* original C++ signature */
    flags: TabBarFlags
    # ImGuiID             ID;    /* original C++ signature */
    id_: ID  # Zero for tab-bars used by docking
    # ImGuiID             SelectedTabId;    /* original C++ signature */
    selected_tab_id: ID  # Selected tab/window
    # ImGuiID             NextSelectedTabId;    /* original C++ signature */
    next_selected_tab_id: ID  # Next selected tab/window. Will also trigger a scrolling animation
    # ImGuiID             VisibleTabId;    /* original C++ signature */
    visible_tab_id: ID  # Can occasionally be != SelectedTabId (e.g. when previewing contents for CTRL+TAB preview)
    # int                 CurrFrameVisible;    /* original C++ signature */
    curr_frame_visible: int
    # int                 PrevFrameVisible;    /* original C++ signature */
    prev_frame_visible: int
    # ImRect              BarRect;    /* original C++ signature */
    bar_rect: ImRect
    # float               CurrTabsContentsHeight;    /* original C++ signature */
    curr_tabs_contents_height: float
    # float               PrevTabsContentsHeight;    /* original C++ signature */
    prev_tabs_contents_height: float  # Record the height of contents submitted below the tab bar
    # float               WidthAllTabs;    /* original C++ signature */
    width_all_tabs: float  # Actual width of all tabs (locked during layout)
    # float               WidthAllTabsIdeal;    /* original C++ signature */
    width_all_tabs_ideal: float  # Ideal width if all tabs were visible and not clipped
    # float               ScrollingAnim;    /* original C++ signature */
    scrolling_anim: float
    # float               ScrollingTarget;    /* original C++ signature */
    scrolling_target: float
    # float               ScrollingTargetDistToVisibility;    /* original C++ signature */
    scrolling_target_dist_to_visibility: float
    # float               ScrollingSpeed;    /* original C++ signature */
    scrolling_speed: float
    # float               ScrollingRectMinX;    /* original C++ signature */
    scrolling_rect_min_x: float
    # float               ScrollingRectMaxX;    /* original C++ signature */
    scrolling_rect_max_x: float
    # float               SeparatorMinX;    /* original C++ signature */
    separator_min_x: float
    # float               SeparatorMaxX;    /* original C++ signature */
    separator_max_x: float
    # ImGuiID             ReorderRequestTabId;    /* original C++ signature */
    reorder_request_tab_id: ID
    # ImS16               ReorderRequestOffset;    /* original C++ signature */
    reorder_request_offset: ImS16
    # ImS8                BeginCount;    /* original C++ signature */
    begin_count: ImS8
    # bool                WantLayout;    /* original C++ signature */
    want_layout: bool
    # bool                VisibleTabWasSubmitted;    /* original C++ signature */
    visible_tab_was_submitted: bool
    # bool                TabsAddedNew;    /* original C++ signature */
    tabs_added_new: bool  # Set to True when a new tab item or button has been added to the tab bar during last frame
    # ImS16               TabsActiveCount;    /* original C++ signature */
    tabs_active_count: ImS16  # Number of tabs submitted this frame.
    # ImS16               LastTabItemIdx;    /* original C++ signature */
    last_tab_item_idx: ImS16  # Index of last BeginTabItem() tab for use by EndTabItem()
    # float               ItemSpacingY;    /* original C++ signature */
    item_spacing_y: float
    # ImVec2              FramePadding;    /* original C++ signature */
    frame_padding: ImVec2  # style.FramePadding locked at the time of BeginTabBar()
    # ImVec2              BackupCursorPos;    /* original C++ signature */
    backup_cursor_pos: ImVec2
    # ImGuiTextBuffer     TabsNames;    /* original C++ signature */
    tabs_names: TextBuffer  # For non-docking tab bar we re-append names in a contiguous buffer.

    # ImGuiTabBar();    /* original C++ signature */
    def __init__(self) -> None:
        pass

# -----------------------------------------------------------------------------
# [SECTION] Table support
# -----------------------------------------------------------------------------

# Our current column maximum is 64 but we may raise that in the future.

class TableColumn:
    """[Internal] sizeof() ~ 112
    We use the terminology "Enabled" to refer to a column that is not Hidden by user/api.
    We use the terminology "Clipped" to refer to a column that is out of sight because of scrolling/clipping.
    This is in contrast with some user-facing api such as IsItemVisible() / IsRectVisible() which use "Visible" to mean "not clipped".
    """

    # ImGuiTableColumnFlags   Flags;    /* original C++ signature */
    flags: TableColumnFlags  # Flags after some patching (not directly same as provided by user). See ImGuiTableColumnFlags_
    # float                   WidthGiven;    /* original C++ signature */
    width_given: float  # Final/actual width visible == (MaxX - MinX), locked in TableUpdateLayout(). May be > WidthRequest to honor minimum width, may be < WidthRequest to honor shrinking columns down in tight space.
    # float                   MinX;    /* original C++ signature */
    min_x: float  # Absolute positions
    # float                   MaxX;    /* original C++ signature */
    max_x: float
    # float                   WidthRequest;    /* original C++ signature */
    width_request: float  # Master width absolute value when !(Flags & _WidthStretch). When Stretch this is derived every frame from StretchWeight in TableUpdateLayout()
    # float                   WidthAuto;    /* original C++ signature */
    width_auto: float  # Automatic width
    # float                   StretchWeight;    /* original C++ signature */
    stretch_weight: float  # Master width weight when (Flags & _WidthStretch). Often around ~1.0 initially.
    # float                   InitStretchWeightOrWidth;    /* original C++ signature */
    init_stretch_weight_or_width: float  # Value passed to TableSetupColumn(). For Width it is a content width (_without padding_).
    # ImRect                  ClipRect;    /* original C++ signature */
    clip_rect: ImRect  # Clipping rectangle for the column
    # ImGuiID                 UserID;    /* original C++ signature */
    user_id: ID  # Optional, value passed to TableSetupColumn()
    # float                   WorkMinX;    /* original C++ signature */
    work_min_x: float  # Contents region min ~(MinX + CellPaddingX + CellSpacingX1) == cursor start position when entering column
    # float                   WorkMaxX;    /* original C++ signature */
    work_max_x: float  # Contents region max ~(MaxX - CellPaddingX - CellSpacingX2)
    # float                   ItemWidth;    /* original C++ signature */
    item_width: float  # Current item width for the column, preserved across rows
    # float                   ContentMaxXFrozen;    /* original C++ signature */
    content_max_x_frozen: float  # Contents maximum position for frozen rows (apart from headers), from which we can infer content width.
    # float                   ContentMaxXUnfrozen;    /* original C++ signature */
    content_max_x_unfrozen: float
    # float                   ContentMaxXHeadersUsed;    /* original C++ signature */
    content_max_x_headers_used: float  # Contents maximum position for headers rows (regardless of freezing). TableHeader() automatically softclip itself + report ideal desired size, to avoid creating extraneous draw calls
    # float                   ContentMaxXHeadersIdeal;    /* original C++ signature */
    content_max_x_headers_ideal: float
    # ImS16                   NameOffset;    /* original C++ signature */
    name_offset: ImS16  # Offset into parent ColumnsNames[]
    # ImGuiTableColumnIdx     DisplayOrder;    /* original C++ signature */
    display_order: TableColumnIdx  # Index within Table's IndexToDisplayOrder[] (column may be reordered by users)
    # ImGuiTableColumnIdx     IndexWithinEnabledSet;    /* original C++ signature */
    index_within_enabled_set: TableColumnIdx  # Index within enabled/visible set (<= IndexToDisplayOrder)
    # ImGuiTableColumnIdx     PrevEnabledColumn;    /* original C++ signature */
    prev_enabled_column: TableColumnIdx  # Index of prev enabled/visible column within Columns[], -1 if first enabled/visible column
    # ImGuiTableColumnIdx     NextEnabledColumn;    /* original C++ signature */
    next_enabled_column: TableColumnIdx  # Index of next enabled/visible column within Columns[], -1 if last enabled/visible column
    # ImGuiTableColumnIdx     SortOrder;    /* original C++ signature */
    sort_order: TableColumnIdx  # Index of this column within sort specs, -1 if not sorting on this column, 0 for single-sort, may be >0 on multi-sort
    # ImGuiTableDrawChannelIdx DrawChannelCurrent;    /* original C++ signature */
    draw_channel_current: TableDrawChannelIdx  # Index within DrawSplitter.Channels[]
    # ImGuiTableDrawChannelIdx DrawChannelFrozen;    /* original C++ signature */
    draw_channel_frozen: TableDrawChannelIdx  # Draw channels for frozen rows (often headers)
    # ImGuiTableDrawChannelIdx DrawChannelUnfrozen;    /* original C++ signature */
    draw_channel_unfrozen: TableDrawChannelIdx  # Draw channels for unfrozen rows
    # bool                    IsEnabled;    /* original C++ signature */
    is_enabled: bool  # IsUserEnabled && (Flags & ImGuiTableColumnFlags_Disabled) == 0
    # bool                    IsUserEnabled;    /* original C++ signature */
    is_user_enabled: bool  # Is the column not marked Hidden by the user? (unrelated to being off view, e.g. clipped by scrolling).
    # bool                    IsUserEnabledNextFrame;    /* original C++ signature */
    is_user_enabled_next_frame: bool
    # bool                    IsVisibleX;    /* original C++ signature */
    is_visible_x: bool  # Is actually in view (e.g. overlapping the host window clipping rectangle, not scrolled).
    # bool                    IsVisibleY;    /* original C++ signature */
    is_visible_y: bool
    # bool                    IsRequestOutput;    /* original C++ signature */
    is_request_output: bool  # Return value for TableSetColumnIndex() / TableNextColumn(): whether we request user to output contents or not.
    # bool                    IsSkipItems;    /* original C++ signature */
    is_skip_items: bool  # Do we want item submissions to this column to be completely ignored (no layout will happen).
    # bool                    IsPreserveWidthAuto;    /* original C++ signature */
    is_preserve_width_auto: bool
    # ImS8                    NavLayerCurrent;    /* original C++ signature */
    nav_layer_current: ImS8  # ImGuiNavLayer in 1 byte
    # ImU8                    AutoFitQueue;    /* original C++ signature */
    auto_fit_queue: ImU8  # Queue of 8 values for the next 8 frames to request auto-fit
    # ImU8                    CannotSkipItemsQueue;    /* original C++ signature */
    cannot_skip_items_queue: ImU8  # Queue of 8 values for the next 8 frames to disable Clipped/SkipItem
    # ImU8                    SortDirectionsAvailList;    /* original C++ signature */
    sort_directions_avail_list: ImU8  # Ordered list of available sort directions (2-bits each, total 8-bits)

    # ImGuiTableColumn()    /* original C++ signature */
    #     {
    #         memset(this, 0, sizeof(*this));
    #         StretchWeight = WidthRequest = -1.0f;
    #         NameOffset = -1;
    #         DisplayOrder = IndexWithinEnabledSet = -1;
    #         PrevEnabledColumn = NextEnabledColumn = -1;
    #         SortOrder = -1;
    #         SortDirection = ImGuiSortDirection_None;
    #         DrawChannelCurrent = DrawChannelFrozen = DrawChannelUnfrozen = (ImU8)-1;
    #     }
    def __init__(self) -> None:
        pass

class TableCellData:
    """Transient cell data stored per row.
    sizeof() ~ 6
    """

    # ImU32                       BgColor;    /* original C++ signature */
    bg_color: ImU32  # Actual color
    # ImGuiTableColumnIdx         Column;    /* original C++ signature */
    column: TableColumnIdx  # Column number
    # ImGuiTableCellData(ImU32 BgColor = ImU32(), ImGuiTableColumnIdx Column = ImGuiTableColumnIdx());    /* original C++ signature */
    def __init__(
        self, bg_color: ImU32 = ImU32(), column: TableColumnIdx = TableColumnIdx()
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class TableInstanceData:
    """Per-instance data that needs preserving across frames (seemingly most others do not need to be preserved aside from debug needs. Does that means they could be moved to ImGuiTableTempData?)
    sizeof() ~ 24 bytes
    """

    # ImGuiID                     TableInstanceID;    /* original C++ signature */
    table_instance_id: ID
    # float                       LastOuterHeight;    /* original C++ signature */
    last_outer_height: float  # Outer height from last frame
    # float                       LastTopHeadersRowHeight;    /* original C++ signature */
    last_top_headers_row_height: float  # Height of first consecutive header rows from last frame (FIXME: this is used assuming consecutive headers are in same frozen set)
    # float                       LastFrozenHeight;    /* original C++ signature */
    last_frozen_height: float  # Height of frozen section from last frame
    # int                         HoveredRowLast;    /* original C++ signature */
    hovered_row_last: int  # Index of row which was hovered last frame.
    # int                         HoveredRowNext;    /* original C++ signature */
    hovered_row_next: int  # Index of row hovered this frame, set after encountering it.

    # ImGuiTableInstanceData()    { TableInstanceID = 0; LastOuterHeight = LastTopHeadersRowHeight = LastFrozenHeight = 0.0f; HoveredRowLast = HoveredRowNext = -1; }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class Table:
    """FIXME-TABLE: more transient data could be stored in a stacked ImGuiTableTempData: e.g. SortSpecs, incoming RowData
    sizeof() ~ 580 bytes + heap allocs described in TableBeginInitMemory()
    """

    # ImGuiID                     ID;    /* original C++ signature */
    id_: ID
    # ImGuiTableFlags             Flags;    /* original C++ signature */
    flags: TableFlags
    # void*                       RawData;    /* original C++ signature */
    raw_data: Any  # Single allocation to hold Columns[], DisplayOrderToIndex[] and RowCellData[]
    # ImGuiTableTempData*         TempData;    /* original C++ signature */
    temp_data: TableTempData  # Transient data while table is active. Point within g.CurrentTableStack[]
    # ImGuiTableFlags             SettingsLoadedFlags;    /* original C++ signature */
    settings_loaded_flags: TableFlags  # Which data were loaded from the .ini file (e.g. when order is not altered we won't save order)
    # int                         SettingsOffset;    /* original C++ signature */
    settings_offset: int  # Offset in g.SettingsTables
    # int                         LastFrameActive;    /* original C++ signature */
    last_frame_active: int
    # int                         ColumnsCount;    /* original C++ signature */
    columns_count: int  # Number of columns declared in BeginTable()
    # int                         CurrentRow;    /* original C++ signature */
    current_row: int
    # int                         CurrentColumn;    /* original C++ signature */
    current_column: int
    # ImS16                       InstanceCurrent;    /* original C++ signature */
    instance_current: ImS16  # Count of BeginTable() calls with same ID in the same frame (generally 0). This is a little bit similar to BeginCount for a window, but multiple table with same ID look are multiple tables, they are just synched.
    # ImS16                       InstanceInteracted;    /* original C++ signature */
    instance_interacted: ImS16  # Mark which instance (generally 0) of the same ID is being interacted with
    # float                       RowPosY1;    /* original C++ signature */
    row_pos_y1: float
    # float                       RowPosY2;    /* original C++ signature */
    row_pos_y2: float
    # float                       RowMinHeight;    /* original C++ signature */
    row_min_height: float  # Height submitted to TableNextRow()
    # float                       RowCellPaddingY;    /* original C++ signature */
    row_cell_padding_y: float  # Top and bottom padding. Reloaded during row change.
    # float                       RowTextBaseline;    /* original C++ signature */
    row_text_baseline: float
    # float                       RowIndentOffsetX;    /* original C++ signature */
    row_indent_offset_x: float
    # int                         RowBgColorCounter;    /* original C++ signature */
    row_bg_color_counter: int  # Counter for alternating background colors (can be fast-forwarded by e.g clipper), not same as CurrentRow because header rows typically don't increase this.
    # ImU32                       RowBgColor[2];    /* original C++ signature */
    row_bg_color: np.ndarray  # ndarray[type=ImU32, size=2]  # Background color override for current row.
    # ImU32                       BorderColorStrong;    /* original C++ signature */
    border_color_strong: ImU32
    # ImU32                       BorderColorLight;    /* original C++ signature */
    border_color_light: ImU32
    # float                       BorderX1;    /* original C++ signature */
    border_x1: float
    # float                       BorderX2;    /* original C++ signature */
    border_x2: float
    # float                       HostIndentX;    /* original C++ signature */
    host_indent_x: float
    # float                       MinColumnWidth;    /* original C++ signature */
    min_column_width: float
    # float                       OuterPaddingX;    /* original C++ signature */
    outer_padding_x: float
    # float                       CellPaddingX;    /* original C++ signature */
    cell_padding_x: float  # Padding from each borders. Locked in BeginTable()/Layout.
    # float                       CellSpacingX1;    /* original C++ signature */
    cell_spacing_x1: float  # Spacing between non-bordered cells. Locked in BeginTable()/Layout.
    # float                       CellSpacingX2;    /* original C++ signature */
    cell_spacing_x2: float
    # float                       InnerWidth;    /* original C++ signature */
    inner_width: float  # User value passed to BeginTable(), see comments at the top of BeginTable() for details.
    # float                       ColumnsGivenWidth;    /* original C++ signature */
    columns_given_width: float  # Sum of current column width
    # float                       ColumnsAutoFitWidth;    /* original C++ signature */
    columns_auto_fit_width: float  # Sum of ideal column width in order nothing to be clipped, used for auto-fitting and content width submission in outer window
    # float                       ColumnsStretchSumWeights;    /* original C++ signature */
    columns_stretch_sum_weights: float  # Sum of weight of all enabled stretching columns
    # float                       ResizedColumnNextWidth;    /* original C++ signature */
    resized_column_next_width: float
    # float                       ResizeLockMinContentsX2;    /* original C++ signature */
    resize_lock_min_contents_x2: float  # Lock minimum contents width while resizing down in order to not create feedback loops. But we allow growing the table.
    # float                       RefScale;    /* original C++ signature */
    ref_scale: float  # Reference scale to be able to rescale columns on font/dpi changes.
    # float                       AngledHeadersHeight;    /* original C++ signature */
    angled_headers_height: float  # Set by TableAngledHeadersRow(), used in TableUpdateLayout()
    # float                       AngledHeadersSlope;    /* original C++ signature */
    angled_headers_slope: float  # Set by TableAngledHeadersRow(), used in TableUpdateLayout()
    # ImRect                      OuterRect;    /* original C++ signature */
    outer_rect: ImRect  # Note: for non-scrolling table, OuterRect.Max.y is often FLT_MAX until EndTable(), unless a height has been specified in BeginTable().
    # ImRect                      InnerRect;    /* original C++ signature */
    inner_rect: ImRect  # InnerRect but without decoration. As with OuterRect, for non-scrolling tables, InnerRect.Max.y is
    # ImRect                      WorkRect;    /* original C++ signature */
    work_rect: ImRect
    # ImRect                      InnerClipRect;    /* original C++ signature */
    inner_clip_rect: ImRect
    # ImRect                      BgClipRect;    /* original C++ signature */
    bg_clip_rect: ImRect  # We use this to cpu-clip cell background color fill, evolve during the frame as we cross frozen rows boundaries
    # ImRect                      Bg0ClipRectForDrawCmd;    /* original C++ signature */
    bg0_clip_rect_for_draw_cmd: ImRect  # Actual ImDrawCmd clip rect for BG0/1 channel. This tends to be == OuterWindow->ClipRect at BeginTable() because output in BG0/BG1 is cpu-clipped
    # ImRect                      Bg2ClipRectForDrawCmd;    /* original C++ signature */
    bg2_clip_rect_for_draw_cmd: ImRect  # Actual ImDrawCmd clip rect for BG2 channel. This tends to be a correct, tight-fit, because output to BG2 are done by widgets relying on regular ClipRect.
    # ImRect                      HostClipRect;    /* original C++ signature */
    host_clip_rect: ImRect  # This is used to check if we can eventually merge our columns draw calls into the current draw call of the current window.
    # ImRect                      HostBackupInnerClipRect;    /* original C++ signature */
    host_backup_inner_clip_rect: ImRect  # Backup of InnerWindow->ClipRect during PushTableBackground()/PopTableBackground()
    # ImGuiWindow*                OuterWindow;    /* original C++ signature */
    outer_window: Window  # Parent window for the table
    # ImGuiWindow*                InnerWindow;    /* original C++ signature */
    inner_window: Window  # Window holding the table data (== OuterWindow or a child window)
    # ImGuiTextBuffer             ColumnsNames;    /* original C++ signature */
    columns_names: TextBuffer  # Contiguous buffer holding columns names
    # ImDrawListSplitter*         DrawSplitter;    /* original C++ signature */
    draw_splitter: ImDrawListSplitter  # Shortcut to TempData->DrawSplitter while in table. Isolate draw commands per columns to avoid switching clip rect constantly
    # ImGuiTableInstanceData      InstanceDataFirst;    /* original C++ signature */
    instance_data_first: TableInstanceData
    # ImVector<ImGuiTableInstanceData>    InstanceDataExtra;    /* original C++ signature */
    instance_data_extra: ImVector_TableInstanceData  # FIXME-OPT: Using a small-vector pattern would be good.
    # ImGuiTableColumnSortSpecs   SortSpecsSingle;    /* original C++ signature */
    sort_specs_single: TableColumnSortSpecs
    # ImVector<ImGuiTableColumnSortSpecs> SortSpecsMulti;    /* original C++ signature */
    sort_specs_multi: ImVector_TableColumnSortSpecs  # FIXME-OPT: Using a small-vector pattern would be good.
    # ImGuiTableSortSpecs         SortSpecs;    /* original C++ signature */
    sort_specs: TableSortSpecs  # Public facing sorts specs, this is what we return in TableGetSortSpecs()
    # ImGuiTableColumnIdx         SortSpecsCount;    /* original C++ signature */
    sort_specs_count: TableColumnIdx
    # ImGuiTableColumnIdx         ColumnsEnabledCount;    /* original C++ signature */
    columns_enabled_count: TableColumnIdx  # Number of enabled columns (<= ColumnsCount)
    # ImGuiTableColumnIdx         ColumnsEnabledFixedCount;    /* original C++ signature */
    columns_enabled_fixed_count: TableColumnIdx  # Number of enabled columns (<= ColumnsCount)
    # ImGuiTableColumnIdx         DeclColumnsCount;    /* original C++ signature */
    decl_columns_count: TableColumnIdx  # Count calls to TableSetupColumn()
    # ImGuiTableColumnIdx         AngledHeadersCount;    /* original C++ signature */
    angled_headers_count: TableColumnIdx  # Count columns with angled headers
    # ImGuiTableColumnIdx         HoveredColumnBody;    /* original C++ signature */
    hovered_column_body: TableColumnIdx  # Index of column whose visible region is being hovered. Important: == ColumnsCount when hovering empty region after the right-most column!
    # ImGuiTableColumnIdx         HoveredColumnBorder;    /* original C++ signature */
    hovered_column_border: TableColumnIdx  # Index of column whose right-border is being hovered (for resizing).
    # ImGuiTableColumnIdx         HighlightColumnHeader;    /* original C++ signature */
    highlight_column_header: TableColumnIdx  # Index of column which should be highlighted.
    # ImGuiTableColumnIdx         AutoFitSingleColumn;    /* original C++ signature */
    auto_fit_single_column: TableColumnIdx  # Index of single column requesting auto-fit.
    # ImGuiTableColumnIdx         ResizedColumn;    /* original C++ signature */
    resized_column: TableColumnIdx  # Index of column being resized. Reset when InstanceCurrent==0.
    # ImGuiTableColumnIdx         LastResizedColumn;    /* original C++ signature */
    last_resized_column: TableColumnIdx  # Index of column being resized from previous frame.
    # ImGuiTableColumnIdx         HeldHeaderColumn;    /* original C++ signature */
    held_header_column: TableColumnIdx  # Index of column header being held.
    # ImGuiTableColumnIdx         ReorderColumn;    /* original C++ signature */
    reorder_column: TableColumnIdx  # Index of column being reordered. (not cleared)
    # ImGuiTableColumnIdx         ReorderColumnDir;    /* original C++ signature */
    reorder_column_dir: TableColumnIdx  # -1 or +1
    # ImGuiTableColumnIdx         LeftMostEnabledColumn;    /* original C++ signature */
    left_most_enabled_column: TableColumnIdx  # Index of left-most non-hidden column.
    # ImGuiTableColumnIdx         RightMostEnabledColumn;    /* original C++ signature */
    right_most_enabled_column: TableColumnIdx  # Index of right-most non-hidden column.
    # ImGuiTableColumnIdx         LeftMostStretchedColumn;    /* original C++ signature */
    left_most_stretched_column: TableColumnIdx  # Index of left-most stretched column.
    # ImGuiTableColumnIdx         RightMostStretchedColumn;    /* original C++ signature */
    right_most_stretched_column: TableColumnIdx  # Index of right-most stretched column.
    # ImGuiTableColumnIdx         ContextPopupColumn;    /* original C++ signature */
    context_popup_column: TableColumnIdx  # Column right-clicked on, of -1 if opening context menu from a neutral/empty spot
    # ImGuiTableColumnIdx         FreezeRowsRequest;    /* original C++ signature */
    freeze_rows_request: TableColumnIdx  # Requested frozen rows count
    # ImGuiTableColumnIdx         FreezeRowsCount;    /* original C++ signature */
    freeze_rows_count: TableColumnIdx  # Actual frozen row count (== FreezeRowsRequest, or == 0 when no scrolling offset)
    # ImGuiTableColumnIdx         FreezeColumnsRequest;    /* original C++ signature */
    freeze_columns_request: TableColumnIdx  # Requested frozen columns count
    # ImGuiTableColumnIdx         FreezeColumnsCount;    /* original C++ signature */
    freeze_columns_count: TableColumnIdx  # Actual frozen columns count (== FreezeColumnsRequest, or == 0 when no scrolling offset)
    # ImGuiTableColumnIdx         RowCellDataCurrent;    /* original C++ signature */
    row_cell_data_current: TableColumnIdx  # Index of current RowCellData[] entry in current row
    # ImGuiTableDrawChannelIdx    DummyDrawChannel;    /* original C++ signature */
    dummy_draw_channel: TableDrawChannelIdx  # Redirect non-visible columns here.
    # ImGuiTableDrawChannelIdx    Bg2DrawChannelCurrent;    /* original C++ signature */
    bg2_draw_channel_current: TableDrawChannelIdx  # For Selectable() and other widgets drawing across columns after the freezing line. Index within DrawSplitter.Channels[]
    # ImGuiTableDrawChannelIdx    Bg2DrawChannelUnfrozen;    /* original C++ signature */
    bg2_draw_channel_unfrozen: TableDrawChannelIdx
    # bool                        IsLayoutLocked;    /* original C++ signature */
    is_layout_locked: bool  # Set by TableUpdateLayout() which is called when beginning the first row.
    # bool                        IsInsideRow;    /* original C++ signature */
    is_inside_row: bool  # Set when inside TableBeginRow()/TableEndRow().
    # bool                        IsInitializing;    /* original C++ signature */
    is_initializing: bool
    # bool                        IsSortSpecsDirty;    /* original C++ signature */
    is_sort_specs_dirty: bool
    # bool                        IsUsingHeaders;    /* original C++ signature */
    is_using_headers: bool  # Set when the first row had the ImGuiTableRowFlags_Headers flag.
    # bool                        IsContextPopupOpen;    /* original C++ signature */
    is_context_popup_open: bool  # Set when default context menu is open (also see: ContextPopupColumn, InstanceInteracted).
    # bool                        DisableDefaultContextMenu;    /* original C++ signature */
    disable_default_context_menu: bool  # Disable default context menu contents. You may submit your own using TableBeginContextMenuPopup()/EndPopup()
    # bool                        IsSettingsRequestLoad;    /* original C++ signature */
    is_settings_request_load: bool
    # bool                        IsSettingsDirty;    /* original C++ signature */
    is_settings_dirty: bool  # Set when table settings have changed and needs to be reported into ImGuiTableSetttings data.
    # bool                        IsDefaultDisplayOrder;    /* original C++ signature */
    is_default_display_order: bool  # Set when display order is unchanged from default (DisplayOrder contains 0...Count-1)
    # bool                        IsResetAllRequest;    /* original C++ signature */
    is_reset_all_request: bool
    # bool                        IsResetDisplayOrderRequest;    /* original C++ signature */
    is_reset_display_order_request: bool
    # bool                        IsUnfrozenRows;    /* original C++ signature */
    is_unfrozen_rows: bool  # Set when we got past the frozen row.
    # bool                        IsDefaultSizingPolicy;    /* original C++ signature */
    is_default_sizing_policy: bool  # Set if user didn't explicitly set a sizing policy in BeginTable()
    # bool                        IsActiveIdAliveBeforeTable;    /* original C++ signature */
    is_active_id_alive_before_table: bool
    # bool                        IsActiveIdInTable;    /* original C++ signature */
    is_active_id_in_table: bool
    # bool                        HasScrollbarYCurr;    /* original C++ signature */
    has_scrollbar_y_curr: bool  # Whether ANY instance of this table had a vertical scrollbar during the current frame.
    # bool                        HasScrollbarYPrev;    /* original C++ signature */
    has_scrollbar_y_prev: bool  # Whether ANY instance of this table had a vertical scrollbar during the previous.
    # bool                        MemoryCompacted;    /* original C++ signature */
    memory_compacted: bool
    # bool                        HostSkipItems;    /* original C++ signature */
    host_skip_items: bool  # Backup of InnerWindow->SkipItem at the end of BeginTable(), because we will overwrite InnerWindow->SkipItem on a per-column basis

    # ImGuiTable()                { memset(this, 0, sizeof(*this)); LastFrameActive = -1; }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class TableTempData:
    """Transient data that are only needed between BeginTable() and EndTable(), those buffers are shared (1 per level of stacked table).
    - Accessing those requires chasing an extra pointer so for very frequently used data we leave them in the main table structure.
    - We also leave out of this structure data that tend to be particularly useful for debugging/metrics.
    sizeof() ~ 120 bytes.
    """

    # int                         TableIndex;    /* original C++ signature */
    table_index: int  # Index in g.Tables.Buf[] pool
    # float                       LastTimeActive;    /* original C++ signature */
    last_time_active: float  # Last timestamp this structure was used
    # float                       AngledheadersExtraWidth;    /* original C++ signature */
    angledheaders_extra_width: float  # Used in EndTable()

    # ImVec2                      UserOuterSize;    /* original C++ signature */
    user_outer_size: ImVec2  # outer_size.x passed to BeginTable()
    # ImDrawListSplitter          DrawSplitter;    /* original C++ signature */
    draw_splitter: ImDrawListSplitter

    # ImRect                      HostBackupWorkRect;    /* original C++ signature */
    host_backup_work_rect: ImRect  # Backup of InnerWindow->WorkRect at the end of BeginTable()
    # ImRect                      HostBackupParentWorkRect;    /* original C++ signature */
    host_backup_parent_work_rect: ImRect  # Backup of InnerWindow->ParentWorkRect at the end of BeginTable()
    # ImVec2                      HostBackupPrevLineSize;    /* original C++ signature */
    host_backup_prev_line_size: ImVec2  # Backup of InnerWindow->DC.PrevLineSize at the end of BeginTable()
    # ImVec2                      HostBackupCurrLineSize;    /* original C++ signature */
    host_backup_curr_line_size: ImVec2  # Backup of InnerWindow->DC.CurrLineSize at the end of BeginTable()
    # ImVec2                      HostBackupCursorMaxPos;    /* original C++ signature */
    host_backup_cursor_max_pos: ImVec2  # Backup of InnerWindow->DC.CursorMaxPos at the end of BeginTable()
    # ImVec1                      HostBackupColumnsOffset;    /* original C++ signature */
    host_backup_columns_offset: ImVec1  # Backup of OuterWindow->DC.ColumnsOffset at the end of BeginTable()
    # float                       HostBackupItemWidth;    /* original C++ signature */
    host_backup_item_width: float  # Backup of OuterWindow->DC.ItemWidth at the end of BeginTable()
    # int                         HostBackupItemWidthStackSize;    /* original C++ signature */
    host_backup_item_width_stack_size: int  # Backup of OuterWindow->DC.ItemWidthStack.Size at the end of BeginTable()

    # ImGuiTableTempData()        { memset(this, 0, sizeof(*this)); LastTimeActive = -1.0f; }    /* original C++ signature */
    def __init__(self) -> None:
        pass

class TableColumnSettings:
    """sizeof() ~ 12"""

    # float                   WidthOrWeight;    /* original C++ signature */
    width_or_weight: float
    # ImGuiID                 UserID;    /* original C++ signature */
    user_id: ID
    # ImGuiTableColumnIdx     Index;    /* original C++ signature */
    index: TableColumnIdx
    # ImGuiTableColumnIdx     DisplayOrder;    /* original C++ signature */
    display_order: TableColumnIdx
    # ImGuiTableColumnIdx     SortOrder;    /* original C++ signature */
    sort_order: TableColumnIdx

    # ImGuiTableColumnSettings()    /* original C++ signature */
    #     {
    #         WidthOrWeight = 0.0f;
    #         UserID = 0;
    #         Index = -1;
    #         DisplayOrder = SortOrder = -1;
    #         SortDirection = ImGuiSortDirection_None;
    #         IsEnabled = 1;
    #         IsStretch = 0;
    #     }
    def __init__(self) -> None:
        pass

class TableSettings:
    """This is designed to be stored in a single ImChunkStream (1 header followed by N ImGuiTableColumnSettings, etc.)"""

    # ImGuiID                     ID;    /* original C++ signature */
    id_: ID  # Set to 0 to invalidate/delete the setting
    # ImGuiTableFlags             SaveFlags;    /* original C++ signature */
    save_flags: TableFlags  # Indicate data we want to save using the Resizable/Reorderable/Sortable/Hideable flags (could be using its own flags..)
    # float                       RefScale;    /* original C++ signature */
    ref_scale: float  # Reference scale to be able to rescale columns on font/dpi changes.
    # ImGuiTableColumnIdx         ColumnsCount;    /* original C++ signature */
    columns_count: TableColumnIdx
    # ImGuiTableColumnIdx         ColumnsCountMax;    /* original C++ signature */
    columns_count_max: TableColumnIdx  # Maximum number of columns this settings instance can store, we can recycle a settings instance with lower number of columns but not higher
    # bool                        WantApply;    /* original C++ signature */
    want_apply: bool  # Set when loaded from .ini data (to enable merging/loading .ini data into an already running context)

    # ImGuiTableSettings()        { memset(this, 0, sizeof(*this)); }    /* original C++ signature */
    def __init__(self) -> None:
        pass
    # ImGuiTableColumnSettings*   GetColumnSettings()     { return (ImGuiTableColumnSettings*)(this + 1); }    /* original C++ signature */
    def get_column_settings(self) -> TableColumnSettings:
        """(private API)"""
        pass

# -----------------------------------------------------------------------------
# [SECTION] ImGui internal API
# No guarantee of forward compatibility here!
# -----------------------------------------------------------------------------

# Windows
# We should always have a CurrentWindow in the stack (there is an implicit "Debug" window)
# If this ever crash because g.CurrentWindow is None it means that either
# - ImGui::NewFrame() has never been called, which is illegal.
# - You are calling ImGui functions after ImGui::EndFrame()/ImGui::Render() and before the next ImGui::NewFrame(), which is also illegal.
# inline    ImGuiWindow*  GetCurrentWindowRead()      { ImGuiContext& g = *GImGui; return g.CurrentWindow; }    /* original C++ signature */
def get_current_window_read() -> Window:
    """(private API)"""
    pass

# IMGUI_API ImGuiWindow*  GetCurrentWindow()          { ImGuiContext& g = *GImGui; g.CurrentWindow->WriteAccessed = true; return g.CurrentWindow; }    /* original C++ signature */
def get_current_window() -> Window:
    pass

# IMGUI_API ImGuiWindow*  FindWindowByID(ImGuiID id);    /* original C++ signature */
def find_window_by_id(id_: ID) -> Window:
    pass

# IMGUI_API ImGuiWindow*  FindWindowByName(const char* name);    /* original C++ signature */
def find_window_by_name(name: str) -> Window:
    pass

# IMGUI_API void          UpdateWindowParentAndRootLinks(ImGuiWindow* window, ImGuiWindowFlags flags, ImGuiWindow* parent_window);    /* original C++ signature */
def update_window_parent_and_root_links(
    window: Window, flags: WindowFlags, parent_window: Window
) -> None:
    pass

# IMGUI_API ImVec2        CalcWindowNextAutoFitSize(ImGuiWindow* window);    /* original C++ signature */
def calc_window_next_auto_fit_size(window: Window) -> ImVec2:
    pass

# IMGUI_API bool          IsWindowChildOf(ImGuiWindow* window, ImGuiWindow* potential_parent, bool popup_hierarchy, bool dock_hierarchy);    /* original C++ signature */
def is_window_child_of(
    window: Window,
    potential_parent: Window,
    popup_hierarchy: bool,
    dock_hierarchy: bool,
) -> bool:
    pass

# IMGUI_API bool          IsWindowWithinBeginStackOf(ImGuiWindow* window, ImGuiWindow* potential_parent);    /* original C++ signature */
def is_window_within_begin_stack_of(window: Window, potential_parent: Window) -> bool:
    pass

# IMGUI_API bool          IsWindowAbove(ImGuiWindow* potential_above, ImGuiWindow* potential_below);    /* original C++ signature */
def is_window_above(potential_above: Window, potential_below: Window) -> bool:
    pass

# IMGUI_API bool          IsWindowNavFocusable(ImGuiWindow* window);    /* original C++ signature */
def is_window_nav_focusable(window: Window) -> bool:
    pass

# IMGUI_API void          SetWindowPos(ImGuiWindow* window, const ImVec2& pos, ImGuiCond cond = 0);    /* original C++ signature */
def set_window_pos(window: Window, pos: ImVec2, cond: Cond = 0) -> None:
    pass

# IMGUI_API void          SetWindowSize(ImGuiWindow* window, const ImVec2& size, ImGuiCond cond = 0);    /* original C++ signature */
def set_window_size(window: Window, size: ImVec2, cond: Cond = 0) -> None:
    pass

# IMGUI_API void          SetWindowCollapsed(ImGuiWindow* window, bool collapsed, ImGuiCond cond = 0);    /* original C++ signature */
def set_window_collapsed(window: Window, collapsed: bool, cond: Cond = 0) -> None:
    pass

# IMGUI_API void          SetWindowHitTestHole(ImGuiWindow* window, const ImVec2& pos, const ImVec2& size);    /* original C++ signature */
def set_window_hit_test_hole(window: Window, pos: ImVec2, size: ImVec2) -> None:
    pass

# IMGUI_API void          SetWindowHiddendAndSkipItemsForCurrentFrame(ImGuiWindow* window);    /* original C++ signature */
def set_window_hiddend_and_skip_items_for_current_frame(window: Window) -> None:
    pass

# inline ImRect           WindowRectAbsToRel(ImGuiWindow* window, const ImRect& r) { ImVec2 off = window->DC.CursorStartPos; return ImRect(r.Min.x - off.x, r.Min.y - off.y, r.Max.x - off.x, r.Max.y - off.y); }    /* original C++ signature */
def window_rect_abs_to_rel(window: Window, r: ImRect) -> ImRect:
    """(private API)"""
    pass

# inline ImRect           WindowRectRelToAbs(ImGuiWindow* window, const ImRect& r) { ImVec2 off = window->DC.CursorStartPos; return ImRect(r.Min.x + off.x, r.Min.y + off.y, r.Max.x + off.x, r.Max.y + off.y); }    /* original C++ signature */
def window_rect_rel_to_abs(window: Window, r: ImRect) -> ImRect:
    """(private API)"""
    pass

# inline ImVec2           WindowPosRelToAbs(ImGuiWindow* window, const ImVec2& p)  { ImVec2 off = window->DC.CursorStartPos; return ImVec2(p.x + off.x, p.y + off.y); }    /* original C++ signature */
def window_pos_rel_to_abs(window: Window, p: ImVec2) -> ImVec2:
    """(private API)"""
    pass

# Windows: Display Order and Focus Order
# IMGUI_API void          FocusWindow(ImGuiWindow* window, ImGuiFocusRequestFlags flags = 0);    /* original C++ signature */
def focus_window(window: Window, flags: FocusRequestFlags = 0) -> None:
    pass

# IMGUI_API void          FocusTopMostWindowUnderOne(ImGuiWindow* under_this_window, ImGuiWindow* ignore_window, ImGuiViewport* filter_viewport, ImGuiFocusRequestFlags flags);    /* original C++ signature */
def focus_top_most_window_under_one(
    under_this_window: Window,
    ignore_window: Window,
    filter_viewport: Viewport,
    flags: FocusRequestFlags,
) -> None:
    pass

# IMGUI_API void          BringWindowToFocusFront(ImGuiWindow* window);    /* original C++ signature */
def bring_window_to_focus_front(window: Window) -> None:
    pass

# IMGUI_API void          BringWindowToDisplayFront(ImGuiWindow* window);    /* original C++ signature */
def bring_window_to_display_front(window: Window) -> None:
    pass

# IMGUI_API void          BringWindowToDisplayBack(ImGuiWindow* window);    /* original C++ signature */
def bring_window_to_display_back(window: Window) -> None:
    pass

# IMGUI_API void          BringWindowToDisplayBehind(ImGuiWindow* window, ImGuiWindow* above_window);    /* original C++ signature */
def bring_window_to_display_behind(window: Window, above_window: Window) -> None:
    pass

# IMGUI_API int           FindWindowDisplayIndex(ImGuiWindow* window);    /* original C++ signature */
def find_window_display_index(window: Window) -> int:
    pass

# IMGUI_API ImGuiWindow*  FindBottomMostVisibleWindowWithinBeginStack(ImGuiWindow* window);    /* original C++ signature */
def find_bottom_most_visible_window_within_begin_stack(window: Window) -> Window:
    pass

# IMGUI_API void          SetCurrentFont(ImFont* font);    /* original C++ signature */
def set_current_font(font: ImFont) -> None:
    """Fonts, drawing"""
    pass

# inline ImFont*          GetDefaultFont() { ImGuiContext& g = *GImGui; return g.IO.FontDefault ? g.IO.FontDefault : g.IO.Fonts->Fonts[0]; }    /* original C++ signature */
def get_default_font() -> ImFont:
    """(private API)"""
    pass

# inline ImDrawList*      GetForegroundDrawList(ImGuiWindow* window) { return GetForegroundDrawList(window->Viewport); }    /* original C++ signature */
def get_foreground_draw_list(window: Window) -> ImDrawList:
    """(private API)"""
    pass

# IMGUI_API void          AddDrawListToDrawDataEx(ImDrawData* draw_data, ImVector<ImDrawList*>* out_list, ImDrawList* draw_list);    /* original C++ signature */
def add_draw_list_to_draw_data_ex(
    draw_data: ImDrawData, out_list: ImVector_ImDrawList_ptr, draw_list: ImDrawList
) -> None:
    pass

# Init
# IMGUI_API void          Initialize();    /* original C++ signature */
def initialize() -> None:
    pass

# IMGUI_API void          Shutdown();        /* original C++ signature */
def shutdown() -> None:
    """Since 1.60 this is a _private_ function. You can call DestroyContext() to destroy the context created by CreateContext()."""
    pass

# NewFrame
# IMGUI_API void          UpdateInputEvents(bool trickle_fast_inputs);    /* original C++ signature */
def update_input_events(trickle_fast_inputs: bool) -> None:
    pass

# IMGUI_API void          UpdateHoveredWindowAndCaptureFlags();    /* original C++ signature */
def update_hovered_window_and_capture_flags() -> None:
    pass

# IMGUI_API void          StartMouseMovingWindow(ImGuiWindow* window);    /* original C++ signature */
def start_mouse_moving_window(window: Window) -> None:
    pass

# IMGUI_API void          StartMouseMovingWindowOrNode(ImGuiWindow* window, ImGuiDockNode* node, bool undock);    /* original C++ signature */
def start_mouse_moving_window_or_node(
    window: Window, node: DockNode, undock: bool
) -> None:
    pass

# IMGUI_API void          UpdateMouseMovingWindowNewFrame();    /* original C++ signature */
def update_mouse_moving_window_new_frame() -> None:
    pass

# IMGUI_API void          UpdateMouseMovingWindowEndFrame();    /* original C++ signature */
def update_mouse_moving_window_end_frame() -> None:
    pass

# Generic context hooks
# IMGUI_API ImGuiID       AddContextHook(ImGuiContext* context, const ImGuiContextHook* hook);    /* original C++ signature */
def add_context_hook(context: Context, hook: ContextHook) -> ID:
    pass

# IMGUI_API void          RemoveContextHook(ImGuiContext* context, ImGuiID hook_to_remove);    /* original C++ signature */
def remove_context_hook(context: Context, hook_to_remove: ID) -> None:
    pass

# IMGUI_API void          CallContextHooks(ImGuiContext* context, ImGuiContextHookType type);    /* original C++ signature */
def call_context_hooks(context: Context, type: ContextHookType) -> None:
    pass

# Viewports
# IMGUI_API void          TranslateWindowsInViewport(ImGuiViewportP* viewport, const ImVec2& old_pos, const ImVec2& new_pos);    /* original C++ signature */
def translate_windows_in_viewport(
    viewport: ViewportP, old_pos: ImVec2, new_pos: ImVec2
) -> None:
    pass

# IMGUI_API void          ScaleWindowsInViewport(ImGuiViewportP* viewport, float scale);    /* original C++ signature */
def scale_windows_in_viewport(viewport: ViewportP, scale: float) -> None:
    pass

# IMGUI_API void          DestroyPlatformWindow(ImGuiViewportP* viewport);    /* original C++ signature */
def destroy_platform_window(viewport: ViewportP) -> None:
    pass

# IMGUI_API void          SetWindowViewport(ImGuiWindow* window, ImGuiViewportP* viewport);    /* original C++ signature */
def set_window_viewport(window: Window, viewport: ViewportP) -> None:
    pass

# IMGUI_API void          SetCurrentViewport(ImGuiWindow* window, ImGuiViewportP* viewport);    /* original C++ signature */
def set_current_viewport(window: Window, viewport: ViewportP) -> None:
    pass

# IMGUI_API const ImGuiPlatformMonitor*   GetViewportPlatformMonitor(ImGuiViewport* viewport);    /* original C++ signature */
def get_viewport_platform_monitor(viewport: Viewport) -> PlatformMonitor:
    pass

# IMGUI_API ImGuiViewportP*               FindHoveredViewportFromPlatformWindowStack(const ImVec2& mouse_platform_pos);    /* original C++ signature */
def find_hovered_viewport_from_platform_window_stack(
    mouse_platform_pos: ImVec2,
) -> ViewportP:
    pass

# Settings
# IMGUI_API void                  MarkIniSettingsDirty();    /* original C++ signature */
@overload
def mark_ini_settings_dirty() -> None:
    pass

# IMGUI_API void                  MarkIniSettingsDirty(ImGuiWindow* window);    /* original C++ signature */
@overload
def mark_ini_settings_dirty(window: Window) -> None:
    pass

# IMGUI_API void                  ClearIniSettings();    /* original C++ signature */
def clear_ini_settings() -> None:
    pass

# IMGUI_API void                  AddSettingsHandler(const ImGuiSettingsHandler* handler);    /* original C++ signature */
def add_settings_handler(handler: SettingsHandler) -> None:
    pass

# IMGUI_API void                  RemoveSettingsHandler(const char* type_name);    /* original C++ signature */
def remove_settings_handler(type_name: str) -> None:
    pass

# IMGUI_API ImGuiSettingsHandler* FindSettingsHandler(const char* type_name);    /* original C++ signature */
def find_settings_handler(type_name: str) -> SettingsHandler:
    pass

# Settings - Windows
# IMGUI_API ImGuiWindowSettings*  CreateNewWindowSettings(const char* name);    /* original C++ signature */
def create_new_window_settings(name: str) -> WindowSettings:
    pass

# IMGUI_API ImGuiWindowSettings*  FindWindowSettingsByID(ImGuiID id);    /* original C++ signature */
def find_window_settings_by_id(id_: ID) -> WindowSettings:
    pass

# IMGUI_API ImGuiWindowSettings*  FindWindowSettingsByWindow(ImGuiWindow* window);    /* original C++ signature */
def find_window_settings_by_window(window: Window) -> WindowSettings:
    pass

# IMGUI_API void                  ClearWindowSettings(const char* name);    /* original C++ signature */
def clear_window_settings(name: str) -> None:
    pass

# IMGUI_API void          LocalizeRegisterEntries(const ImGuiLocEntry* entries, int count);    /* original C++ signature */
def localize_register_entries(entries: LocEntry, count: int) -> None:
    """Localization"""
    pass

# inline const char*      LocalizeGetMsg(ImGuiLocKey key) { ImGuiContext& g = *GImGui; const char* msg = g.LocalizationTable[key]; return msg ? msg : "*Missing Text*"; }    /* original C++ signature */
def localize_get_msg(key: LocKey) -> str:
    """(private API)"""
    pass

# Scrolling
# IMGUI_API void          SetScrollX(ImGuiWindow* window, float scroll_x);    /* original C++ signature */
def set_scroll_x(window: Window, scroll_x: float) -> None:
    pass

# IMGUI_API void          SetScrollY(ImGuiWindow* window, float scroll_y);    /* original C++ signature */
def set_scroll_y(window: Window, scroll_y: float) -> None:
    pass

# IMGUI_API void          SetScrollFromPosX(ImGuiWindow* window, float local_x, float center_x_ratio);    /* original C++ signature */
def set_scroll_from_pos_x(
    window: Window, local_x: float, center_x_ratio: float
) -> None:
    pass

# IMGUI_API void          SetScrollFromPosY(ImGuiWindow* window, float local_y, float center_y_ratio);    /* original C++ signature */
def set_scroll_from_pos_y(
    window: Window, local_y: float, center_y_ratio: float
) -> None:
    pass

# Early work-in-progress API (ScrollToItem() will become public)
# IMGUI_API void          ScrollToItem(ImGuiScrollFlags flags = 0);    /* original C++ signature */
def scroll_to_item(flags: ScrollFlags = 0) -> None:
    pass

# IMGUI_API void          ScrollToRect(ImGuiWindow* window, const ImRect& rect, ImGuiScrollFlags flags = 0);    /* original C++ signature */
def scroll_to_rect(window: Window, rect: ImRect, flags: ScrollFlags = 0) -> None:
    pass

# IMGUI_API ImVec2        ScrollToRectEx(ImGuiWindow* window, const ImRect& rect, ImGuiScrollFlags flags = 0);    /* original C++ signature */
def scroll_to_rect_ex(window: Window, rect: ImRect, flags: ScrollFlags = 0) -> ImVec2:
    pass

# inline void             ScrollToBringRectIntoView(ImGuiWindow* window, const ImRect& rect) { ScrollToRect(window, rect, ImGuiScrollFlags_KeepVisibleEdgeY); }    /* original C++ signature */
def scroll_to_bring_rect_into_view(window: Window, rect: ImRect) -> None:
    """#ifndef IMGUI_DISABLE_OBSOLETE_FUNCTIONS
    (private API)
    """
    pass

##endif

# Basic Accessors
# inline ImGuiItemStatusFlags GetItemStatusFlags(){ ImGuiContext& g = *GImGui; return g.LastItemData.StatusFlags; }    /* original C++ signature */
def get_item_status_flags() -> ItemStatusFlags:
    """(private API)"""
    pass

# inline ImGuiItemFlags   GetItemFlags()  { ImGuiContext& g = *GImGui; return g.LastItemData.InFlags; }    /* original C++ signature */
def get_item_flags() -> ItemFlags:
    """(private API)"""
    pass

# inline ImGuiID          GetActiveID()   { ImGuiContext& g = *GImGui; return g.ActiveId; }    /* original C++ signature */
def get_active_id() -> ID:
    """(private API)"""
    pass

# inline ImGuiID          GetFocusID()    { ImGuiContext& g = *GImGui; return g.NavId; }    /* original C++ signature */
def get_focus_id() -> ID:
    """(private API)"""
    pass

# IMGUI_API void          SetActiveID(ImGuiID id, ImGuiWindow* window);    /* original C++ signature */
def set_active_id(id_: ID, window: Window) -> None:
    pass

# IMGUI_API void          SetFocusID(ImGuiID id, ImGuiWindow* window);    /* original C++ signature */
def set_focus_id(id_: ID, window: Window) -> None:
    pass

# IMGUI_API void          ClearActiveID();    /* original C++ signature */
def clear_active_id() -> None:
    pass

# IMGUI_API ImGuiID       GetHoveredID();    /* original C++ signature */
def get_hovered_id() -> ID:
    pass

# IMGUI_API void          SetHoveredID(ImGuiID id);    /* original C++ signature */
def set_hovered_id(id_: ID) -> None:
    pass

# IMGUI_API void          KeepAliveID(ImGuiID id);    /* original C++ signature */
def keep_alive_id(id_: ID) -> None:
    pass

# IMGUI_API void          MarkItemEdited(ImGuiID id);         /* original C++ signature */
def mark_item_edited(id_: ID) -> None:
    """Mark data associated to given item as "edited", used by IsItemDeactivatedAfterEdit() function."""
    pass

# IMGUI_API void          PushOverrideID(ImGuiID id);         /* original C++ signature */
def push_override_id(id_: ID) -> None:
    """Push given value as-is at the top of the ID stack (whereas PushID combines old and new hashes)"""
    pass

# IMGUI_API ImGuiID       GetIDWithSeed(const char* str_id_begin, const char* str_id_end, ImGuiID seed);    /* original C++ signature */
@overload
def get_id_with_seed(str_id_begin: str, str_id_end: str, seed: ID) -> ID:
    pass

# IMGUI_API ImGuiID       GetIDWithSeed(int n, ImGuiID seed);    /* original C++ signature */
@overload
def get_id_with_seed(n: int, seed: ID) -> ID:
    pass

# IMGUI_API void          ItemSize(const ImVec2& size, float text_baseline_y = -1.0f);    /* original C++ signature */
@overload
def item_size(size: ImVec2, text_baseline_y: float = -1.0) -> None:
    """Basic Helpers for widget code"""
    pass

# inline void             ItemSize(const ImRect& bb, float text_baseline_y = -1.0f) { ItemSize(bb.GetSize(), text_baseline_y); }     /* original C++ signature */
@overload
def item_size(bb: ImRect, text_baseline_y: float = -1.0) -> None:
    """(private API)

    FIXME: This is a misleading API since we expect CursorPos to be bb.Min.
    """
    pass

# IMGUI_API bool          ItemAdd(const ImRect& bb, ImGuiID id, const ImRect* nav_bb = NULL, ImGuiItemFlags extra_flags = 0);    /* original C++ signature */
def item_add(
    bb: ImRect, id_: ID, nav_bb: Optional[ImRect] = None, extra_flags: ItemFlags = 0
) -> bool:
    pass

# IMGUI_API bool          ItemHoverable(const ImRect& bb, ImGuiID id, ImGuiItemFlags item_flags);    /* original C++ signature */
def item_hoverable(bb: ImRect, id_: ID, item_flags: ItemFlags) -> bool:
    pass

# IMGUI_API bool          IsWindowContentHoverable(ImGuiWindow* window, ImGuiHoveredFlags flags = 0);    /* original C++ signature */
def is_window_content_hoverable(window: Window, flags: HoveredFlags = 0) -> bool:
    pass

# IMGUI_API bool          IsClippedEx(const ImRect& bb, ImGuiID id);    /* original C++ signature */
def is_clipped_ex(bb: ImRect, id_: ID) -> bool:
    pass

# IMGUI_API void          SetLastItemData(ImGuiID item_id, ImGuiItemFlags in_flags, ImGuiItemStatusFlags status_flags, const ImRect& item_rect);    /* original C++ signature */
def set_last_item_data(
    item_id: ID, in_flags: ItemFlags, status_flags: ItemStatusFlags, item_rect: ImRect
) -> None:
    pass

# IMGUI_API ImVec2        CalcItemSize(ImVec2 size, float default_w, float default_h);    /* original C++ signature */
def calc_item_size(size: ImVec2, default_w: float, default_h: float) -> ImVec2:
    pass

# IMGUI_API float         CalcWrapWidthForPos(const ImVec2& pos, float wrap_pos_x);    /* original C++ signature */
def calc_wrap_width_for_pos(pos: ImVec2, wrap_pos_x: float) -> float:
    pass

# IMGUI_API void          PushMultiItemsWidths(int components, float width_full);    /* original C++ signature */
def push_multi_items_widths(components: int, width_full: float) -> None:
    pass

# IMGUI_API bool          IsItemToggledSelection();                                       /* original C++ signature */
def is_item_toggled_selection() -> bool:
    """Was the last item selection toggled? (after Selectable(), TreeNode() etc. We only returns toggle _event_ in order to handle clipping correctly)"""
    pass

# IMGUI_API ImVec2        GetContentRegionMaxAbs();    /* original C++ signature */
def get_content_region_max_abs() -> ImVec2:
    pass

# IMGUI_API void          ShrinkWidths(ImGuiShrinkWidthItem* items, int count, float width_excess);    /* original C++ signature */
def shrink_widths(items: ShrinkWidthItem, count: int, width_excess: float) -> None:
    pass

# Parameter stacks (shared)
# IMGUI_API void          PushItemFlag(ImGuiItemFlags option, bool enabled);    /* original C++ signature */
def push_item_flag(option: ItemFlags, enabled: bool) -> None:
    pass

# IMGUI_API void          PopItemFlag();    /* original C++ signature */
def pop_item_flag() -> None:
    pass

# IMGUI_API const ImGuiDataVarInfo* GetStyleVarInfo(ImGuiStyleVar idx);    /* original C++ signature */
def get_style_var_info(idx: StyleVar) -> DataVarInfo:
    pass

# Logging/Capture
# IMGUI_API void          LogBegin(ImGuiLogType type, int auto_open_depth);               /* original C++ signature */
def log_begin(type: LogType, auto_open_depth: int) -> None:
    """-> BeginCapture() when we design v2 api, for now stay under the radar by using the old name."""
    pass

# IMGUI_API void          LogToBuffer(int auto_open_depth = -1);                          /* original C++ signature */
def log_to_buffer(auto_open_depth: int = -1) -> None:
    """Start logging/capturing to internal buffer"""
    pass

# IMGUI_API void          LogRenderedText(const ImVec2* ref_pos, const char* text, const char* text_end = NULL);    /* original C++ signature */
def log_rendered_text(
    ref_pos: ImVec2, text: str, text_end: Optional[str] = None
) -> None:
    pass

# IMGUI_API void          LogSetNextTextDecoration(const char* prefix, const char* suffix);    /* original C++ signature */
def log_set_next_text_decoration(prefix: str, suffix: str) -> None:
    pass

# Popups, Modals, Tooltips
# IMGUI_API bool          BeginChildEx(const char* name, ImGuiID id, const ImVec2& size_arg, ImGuiChildFlags child_flags, ImGuiWindowFlags window_flags);    /* original C++ signature */
def begin_child_ex(
    name: str,
    id_: ID,
    size_arg: ImVec2,
    child_flags: ChildFlags,
    window_flags: WindowFlags,
) -> bool:
    pass

# IMGUI_API void          OpenPopupEx(ImGuiID id, ImGuiPopupFlags popup_flags = ImGuiPopupFlags_None);    /* original C++ signature */
def open_popup_ex(id_: ID, popup_flags: PopupFlags = PopupFlags_None) -> None:
    pass

# IMGUI_API void          ClosePopupToLevel(int remaining, bool restore_focus_to_window_under_popup);    /* original C++ signature */
def close_popup_to_level(
    remaining: int, restore_focus_to_window_under_popup: bool
) -> None:
    pass

# IMGUI_API void          ClosePopupsOverWindow(ImGuiWindow* ref_window, bool restore_focus_to_window_under_popup);    /* original C++ signature */
def close_popups_over_window(
    ref_window: Window, restore_focus_to_window_under_popup: bool
) -> None:
    pass

# IMGUI_API void          ClosePopupsExceptModals();    /* original C++ signature */
def close_popups_except_modals() -> None:
    pass

# IMGUI_API bool          IsPopupOpen(ImGuiID id, ImGuiPopupFlags popup_flags);    /* original C++ signature */
def is_popup_open(id_: ID, popup_flags: PopupFlags) -> bool:
    pass

# IMGUI_API bool          BeginPopupEx(ImGuiID id, ImGuiWindowFlags extra_flags);    /* original C++ signature */
def begin_popup_ex(id_: ID, extra_flags: WindowFlags) -> bool:
    pass

# IMGUI_API bool          BeginTooltipEx(ImGuiTooltipFlags tooltip_flags, ImGuiWindowFlags extra_window_flags);    /* original C++ signature */
def begin_tooltip_ex(
    tooltip_flags: TooltipFlags, extra_window_flags: WindowFlags
) -> bool:
    pass

# IMGUI_API bool          BeginTooltipHidden();    /* original C++ signature */
def begin_tooltip_hidden() -> bool:
    pass

# IMGUI_API ImRect        GetPopupAllowedExtentRect(ImGuiWindow* window);    /* original C++ signature */
def get_popup_allowed_extent_rect(window: Window) -> ImRect:
    pass

# IMGUI_API ImGuiWindow*  GetTopMostPopupModal();    /* original C++ signature */
def get_top_most_popup_modal() -> Window:
    pass

# IMGUI_API ImGuiWindow*  GetTopMostAndVisiblePopupModal();    /* original C++ signature */
def get_top_most_and_visible_popup_modal() -> Window:
    pass

# IMGUI_API ImGuiWindow*  FindBlockingModal(ImGuiWindow* window);    /* original C++ signature */
def find_blocking_modal(window: Window) -> Window:
    pass

# IMGUI_API ImVec2        FindBestWindowPosForPopup(ImGuiWindow* window);    /* original C++ signature */
def find_best_window_pos_for_popup(window: Window) -> ImVec2:
    pass

# IMGUI_API ImVec2        FindBestWindowPosForPopupEx(const ImVec2& ref_pos, const ImVec2& size, ImGuiDir* last_dir, const ImRect& r_outer, const ImRect& r_avoid, ImGuiPopupPositionPolicy policy);    /* original C++ signature */
def find_best_window_pos_for_popup_ex(
    ref_pos: ImVec2,
    size: ImVec2,
    last_dir: Dir,
    r_outer: ImRect,
    r_avoid: ImRect,
    policy: PopupPositionPolicy,
) -> ImVec2:
    pass

# Menus
# IMGUI_API bool          BeginViewportSideBar(const char* name, ImGuiViewport* viewport, ImGuiDir dir, float size, ImGuiWindowFlags window_flags);    /* original C++ signature */
def begin_viewport_side_bar(
    name: str, viewport: Viewport, dir: Dir, size: float, window_flags: WindowFlags
) -> bool:
    pass

# IMGUI_API bool          BeginMenuEx(const char* label, const char* icon, bool enabled = true);    /* original C++ signature */
def begin_menu_ex(label: str, icon: str, enabled: bool = True) -> bool:
    pass

# IMGUI_API bool          MenuItemEx(const char* label, const char* icon, const char* shortcut = NULL, bool selected = false, bool enabled = true);    /* original C++ signature */
def menu_item_ex(
    label: str,
    icon: str,
    shortcut: Optional[str] = None,
    selected: bool = False,
    enabled: bool = True,
) -> bool:
    pass

# Combos
# IMGUI_API bool          BeginComboPopup(ImGuiID popup_id, const ImRect& bb, ImGuiComboFlags flags);    /* original C++ signature */
def begin_combo_popup(popup_id: ID, bb: ImRect, flags: ComboFlags) -> bool:
    pass

# IMGUI_API bool          BeginComboPreview();    /* original C++ signature */
def begin_combo_preview() -> bool:
    pass

# IMGUI_API void          EndComboPreview();    /* original C++ signature */
def end_combo_preview() -> None:
    pass

# Gamepad/Keyboard Navigation
# IMGUI_API void          NavInitWindow(ImGuiWindow* window, bool force_reinit);    /* original C++ signature */
def nav_init_window(window: Window, force_reinit: bool) -> None:
    pass

# IMGUI_API void          NavInitRequestApplyResult();    /* original C++ signature */
def nav_init_request_apply_result() -> None:
    pass

# IMGUI_API bool          NavMoveRequestButNoResultYet();    /* original C++ signature */
def nav_move_request_but_no_result_yet() -> bool:
    pass

# IMGUI_API void          NavMoveRequestSubmit(ImGuiDir move_dir, ImGuiDir clip_dir, ImGuiNavMoveFlags move_flags, ImGuiScrollFlags scroll_flags);    /* original C++ signature */
def nav_move_request_submit(
    move_dir: Dir, clip_dir: Dir, move_flags: NavMoveFlags, scroll_flags: ScrollFlags
) -> None:
    pass

# IMGUI_API void          NavMoveRequestForward(ImGuiDir move_dir, ImGuiDir clip_dir, ImGuiNavMoveFlags move_flags, ImGuiScrollFlags scroll_flags);    /* original C++ signature */
def nav_move_request_forward(
    move_dir: Dir, clip_dir: Dir, move_flags: NavMoveFlags, scroll_flags: ScrollFlags
) -> None:
    pass

# IMGUI_API void          NavMoveRequestResolveWithLastItem(ImGuiNavItemData* result);    /* original C++ signature */
def nav_move_request_resolve_with_last_item(result: NavItemData) -> None:
    pass

# IMGUI_API void          NavMoveRequestResolveWithPastTreeNode(ImGuiNavItemData* result, ImGuiNavTreeNodeData* tree_node_data);    /* original C++ signature */
def nav_move_request_resolve_with_past_tree_node(
    result: NavItemData, tree_node_data: NavTreeNodeData
) -> None:
    pass

# IMGUI_API void          NavMoveRequestCancel();    /* original C++ signature */
def nav_move_request_cancel() -> None:
    pass

# IMGUI_API void          NavMoveRequestApplyResult();    /* original C++ signature */
def nav_move_request_apply_result() -> None:
    pass

# IMGUI_API void          NavMoveRequestTryWrapping(ImGuiWindow* window, ImGuiNavMoveFlags move_flags);    /* original C++ signature */
def nav_move_request_try_wrapping(window: Window, move_flags: NavMoveFlags) -> None:
    pass

# IMGUI_API void          NavClearPreferredPosForAxis(ImGuiAxis axis);    /* original C++ signature */
def nav_clear_preferred_pos_for_axis(axis: Axis) -> None:
    pass

# IMGUI_API void          NavRestoreHighlightAfterMove();    /* original C++ signature */
def nav_restore_highlight_after_move() -> None:
    pass

# IMGUI_API void          NavUpdateCurrentWindowIsScrollPushableX();    /* original C++ signature */
def nav_update_current_window_is_scroll_pushable_x() -> None:
    pass

# IMGUI_API void          SetNavWindow(ImGuiWindow* window);    /* original C++ signature */
def set_nav_window(window: Window) -> None:
    pass

# IMGUI_API void          SetNavID(ImGuiID id, ImGuiNavLayer nav_layer, ImGuiID focus_scope_id, const ImRect& rect_rel);    /* original C++ signature */
def set_nav_id(
    id_: ID, nav_layer: NavLayer, focus_scope_id: ID, rect_rel: ImRect
) -> None:
    pass

# Focus/Activation
# This should be part of a larger set of API: FocusItem(offset = -1), FocusItemByID(id), ActivateItem(offset = -1), ActivateItemByID(id) etc. which are
# much harder to design and implement than expected. I have a couple of private branches on this matter but it's not simple. For now implementing the easy ones.
# IMGUI_API void          FocusItem();                        /* original C++ signature */
def focus_item() -> None:
    """Focus last item (no selection/activation)."""
    pass

# IMGUI_API void          ActivateItemByID(ImGuiID id);       /* original C++ signature */
def activate_item_by_id(id_: ID) -> None:
    """Activate an item by ID (button, checkbox, tree node etc.). Activation is queued and processed on the next frame when the item is encountered again."""
    pass

# Inputs
# FIXME: Eventually we should aim to move e.g. IsActiveIdUsingKey() into IsKeyXXX functions.
# inline bool             IsNamedKey(ImGuiKey key)                                    { return key >= ImGuiKey_NamedKey_BEGIN && key < ImGuiKey_NamedKey_END; }    /* original C++ signature */
def is_named_key(key: Key) -> bool:
    """(private API)"""
    pass

# inline bool             IsNamedKeyOrModKey(ImGuiKey key)                            { return (key >= ImGuiKey_NamedKey_BEGIN && key < ImGuiKey_NamedKey_END) || key == ImGuiMod_Ctrl || key == ImGuiMod_Shift || key == ImGuiMod_Alt || key == ImGuiMod_Super || key == ImGuiMod_Shortcut; }    /* original C++ signature */
def is_named_key_or_mod_key(key: Key) -> bool:
    """(private API)"""
    pass

# inline bool             IsLegacyKey(ImGuiKey key)                                   { return key >= ImGuiKey_LegacyNativeKey_BEGIN && key < ImGuiKey_LegacyNativeKey_END; }    /* original C++ signature */
def is_legacy_key(key: Key) -> bool:
    """(private API)"""
    pass

# inline bool             IsKeyboardKey(ImGuiKey key)                                 { return key >= ImGuiKey_Keyboard_BEGIN && key < ImGuiKey_Keyboard_END; }    /* original C++ signature */
def is_keyboard_key(key: Key) -> bool:
    """(private API)"""
    pass

# inline bool             IsGamepadKey(ImGuiKey key)                                  { return key >= ImGuiKey_Gamepad_BEGIN && key < ImGuiKey_Gamepad_END; }    /* original C++ signature */
def is_gamepad_key(key: Key) -> bool:
    """(private API)"""
    pass

# inline bool             IsMouseKey(ImGuiKey key)                                    { return key >= ImGuiKey_Mouse_BEGIN && key < ImGuiKey_Mouse_END; }    /* original C++ signature */
def is_mouse_key(key: Key) -> bool:
    """(private API)"""
    pass

# inline bool             IsAliasKey(ImGuiKey key)                                    { return key >= ImGuiKey_Aliases_BEGIN && key < ImGuiKey_Aliases_END; }    /* original C++ signature */
def is_alias_key(key: Key) -> bool:
    """(private API)"""
    pass

# inline ImGuiKeyChord    ConvertShortcutMod(ImGuiKeyChord key_chord)                 { ImGuiContext& g = *GImGui; IM_ASSERT_PARANOID(key_chord & ImGuiMod_Shortcut); return (key_chord & ~ImGuiMod_Shortcut) | (g.IO.ConfigMacOSXBehaviors ? ImGuiMod_Super : ImGuiMod_Ctrl); }    /* original C++ signature */
def convert_shortcut_mod(key_chord: KeyChord) -> KeyChord:
    """(private API)"""
    pass

# inline ImGuiKey         ConvertSingleModFlagToKey(ImGuiContext* ctx, ImGuiKey key)    /* original C++ signature */
#     {
#         ImGuiContext& g = *ctx;
#         if (key == ImGuiMod_Ctrl) return ImGuiKey_ReservedForModCtrl;
#         if (key == ImGuiMod_Shift) return ImGuiKey_ReservedForModShift;
#         if (key == ImGuiMod_Alt) return ImGuiKey_ReservedForModAlt;
#         if (key == ImGuiMod_Super) return ImGuiKey_ReservedForModSuper;
#         if (key == ImGuiMod_Shortcut) return (g.IO.ConfigMacOSXBehaviors ? ImGuiKey_ReservedForModSuper : ImGuiKey_ReservedForModCtrl);
#         return key;
#     }
def convert_single_mod_flag_to_key(ctx: Context, key: Key) -> Key:
    """(private API)"""
    pass

# IMGUI_API ImGuiKeyData* GetKeyData(ImGuiContext* ctx, ImGuiKey key);    /* original C++ signature */
@overload
def get_key_data(ctx: Context, key: Key) -> KeyData:
    pass

# inline ImGuiKeyData*    GetKeyData(ImGuiKey key)                                    { ImGuiContext& g = *GImGui; return GetKeyData(&g, key); }    /* original C++ signature */
@overload
def get_key_data(key: Key) -> KeyData:
    """(private API)"""
    pass

# inline ImGuiKey         MouseButtonToKey(ImGuiMouseButton button)                   { IM_ASSERT(button >= 0 && button < ImGuiMouseButton_COUNT); return (ImGuiKey)(ImGuiKey_MouseLeft + button); }    /* original C++ signature */
def mouse_button_to_key(button: MouseButton) -> Key:
    """(private API)"""
    pass

# IMGUI_API bool          IsMouseDragPastThreshold(ImGuiMouseButton button, float lock_threshold = -1.0f);    /* original C++ signature */
def is_mouse_drag_past_threshold(
    button: MouseButton, lock_threshold: float = -1.0
) -> bool:
    pass

# IMGUI_API ImVec2        GetKeyMagnitude2d(ImGuiKey key_left, ImGuiKey key_right, ImGuiKey key_up, ImGuiKey key_down);    /* original C++ signature */
def get_key_magnitude2d(
    key_left: Key, key_right: Key, key_up: Key, key_down: Key
) -> ImVec2:
    pass

# IMGUI_API float         GetNavTweakPressedAmount(ImGuiAxis axis);    /* original C++ signature */
def get_nav_tweak_pressed_amount(axis: Axis) -> float:
    pass

# IMGUI_API int           CalcTypematicRepeatAmount(float t0, float t1, float repeat_delay, float repeat_rate);    /* original C++ signature */
def calc_typematic_repeat_amount(
    t0: float, t1: float, repeat_delay: float, repeat_rate: float
) -> int:
    pass

# IMGUI_API void          GetTypematicRepeatRate(ImGuiInputFlags flags, float* repeat_delay, float* repeat_rate);    /* original C++ signature */
def get_typematic_repeat_rate(
    flags: InputFlags, repeat_delay: float, repeat_rate: float
) -> Tuple[float, float]:
    pass

# IMGUI_API void          TeleportMousePos(const ImVec2& pos);    /* original C++ signature */
def teleport_mouse_pos(pos: ImVec2) -> None:
    pass

# IMGUI_API void          SetActiveIdUsingAllKeyboardKeys();    /* original C++ signature */
def set_active_id_using_all_keyboard_keys() -> None:
    pass

# inline bool             IsActiveIdUsingNavDir(ImGuiDir dir)                         { ImGuiContext& g = *GImGui; return (g.ActiveIdUsingNavDirMask & (1 << dir)) != 0; }    /* original C++ signature */
def is_active_id_using_nav_dir(dir: Dir) -> bool:
    """(private API)"""
    pass

# [EXPERIMENTAL] Low-Level: Key/Input Ownership
# - The idea is that instead of "eating" a given input, we can link to an owner id.
# - Ownership is most often claimed as a result of reacting to a press/down event (but occasionally may be claimed ahead).
# - Input queries can then read input by specifying ImGuiKeyOwner_Any (== 0), ImGuiKeyOwner_None (== -1) or a custom ID.
# - Legacy input queries (without specifying an owner or _Any or _None) are equivalent to using ImGuiKeyOwner_Any (== 0).
# - Input ownership is automatically released on the frame after a key is released. Therefore:
#   - for ownership registration happening as a result of a down/press event, the SetKeyOwner() call may be done once (common case).
#   - for ownership registration happening ahead of a down/press event, the SetKeyOwner() call needs to be made every frame (happens if e.g. claiming ownership on hover).
# - SetItemKeyOwner() is a shortcut for common simple case. A custom widget will probably want to call SetKeyOwner() multiple times directly based on its interaction state.
# - This is marked experimental because not all widgets are fully honoring the Set/Test idioms. We will need to move forward step by step.
#   Please open a GitHub Issue to submit your usage scenario or if there's a use case you need solved.
# IMGUI_API ImGuiID           GetKeyOwner(ImGuiKey key);    /* original C++ signature */
def get_key_owner(key: Key) -> ID:
    pass

# IMGUI_API void              SetKeyOwner(ImGuiKey key, ImGuiID owner_id, ImGuiInputFlags flags = 0);    /* original C++ signature */
def set_key_owner(key: Key, owner_id: ID, flags: InputFlags = 0) -> None:
    pass

# IMGUI_API void              SetKeyOwnersForKeyChord(ImGuiKeyChord key, ImGuiID owner_id, ImGuiInputFlags flags = 0);    /* original C++ signature */
def set_key_owners_for_key_chord(
    key: KeyChord, owner_id: ID, flags: InputFlags = 0
) -> None:
    pass

# IMGUI_API void              SetItemKeyOwner(ImGuiKey key, ImGuiInputFlags flags = 0);               /* original C++ signature */
def set_item_key_owner(key: Key, flags: InputFlags = 0) -> None:
    """Set key owner to last item if it is hovered or active. Equivalent to 'if (IsItemHovered() || IsItemActive()) { SetKeyOwner(key, GetItemID());'."""
    pass

# IMGUI_API bool              TestKeyOwner(ImGuiKey key, ImGuiID owner_id);                           /* original C++ signature */
def test_key_owner(key: Key, owner_id: ID) -> bool:
    """Test that key is either not owned, either owned by 'owner_id'"""
    pass

# inline ImGuiKeyOwnerData*   GetKeyOwnerData(ImGuiContext* ctx, ImGuiKey key)                    { if (key & ImGuiMod_Mask_) key = ConvertSingleModFlagToKey(ctx, key); IM_ASSERT(IsNamedKey(key)); return &ctx->KeysOwnerData[key - ImGuiKey_NamedKey_BEGIN]; }    /* original C++ signature */
def get_key_owner_data(ctx: Context, key: Key) -> KeyOwnerData:
    """(private API)"""
    pass

# [EXPERIMENTAL] High-Level: Input Access functions w/ support for Key/Input Ownership
# - Important: legacy IsKeyPressed(ImGuiKey, bool repeat=True) _DEFAULTS_ to repeat, new IsKeyPressed() requires _EXPLICIT_ ImGuiInputFlags_Repeat flag.
# - Expected to be later promoted to public API, the prototypes are designed to replace existing ones (since owner_id can default to Any == 0)
# - Specifying a value for 'ImGuiID owner' will test that EITHER the key is NOT owned (UNLESS locked), EITHER the key is owned by 'owner'.
#   Legacy functions use ImGuiKeyOwner_Any meaning that they typically ignore ownership, unless a call to SetKeyOwner() explicitly used ImGuiInputFlags_LockThisFrame or ImGuiInputFlags_LockUntilRelease.
# - Binding generators may want to ignore those for now, or suffix them with Ex() until we decide if this gets moved into public API.
# IMGUI_API bool              IsKeyDown(ImGuiKey key, ImGuiID owner_id);    /* original C++ signature */
def is_key_down(key: Key, owner_id: ID) -> bool:
    pass

# IMGUI_API bool              IsKeyPressed(ImGuiKey key, ImGuiID owner_id, ImGuiInputFlags flags = 0);        /* original C++ signature */
def is_key_pressed(key: Key, owner_id: ID, flags: InputFlags = 0) -> bool:
    """Important: when transitioning from old to new IsKeyPressed(): old API has "bool repeat = True", so would default to repeat. New API requiress explicit ImGuiInputFlags_Repeat."""
    pass

# IMGUI_API bool              IsKeyReleased(ImGuiKey key, ImGuiID owner_id);    /* original C++ signature */
def is_key_released(key: Key, owner_id: ID) -> bool:
    pass

# IMGUI_API bool              IsMouseDown(ImGuiMouseButton button, ImGuiID owner_id);    /* original C++ signature */
def is_mouse_down(button: MouseButton, owner_id: ID) -> bool:
    pass

# IMGUI_API bool              IsMouseClicked(ImGuiMouseButton button, ImGuiID owner_id, ImGuiInputFlags flags = 0);    /* original C++ signature */
def is_mouse_clicked(button: MouseButton, owner_id: ID, flags: InputFlags = 0) -> bool:
    pass

# IMGUI_API bool              IsMouseReleased(ImGuiMouseButton button, ImGuiID owner_id);    /* original C++ signature */
def is_mouse_released(button: MouseButton, owner_id: ID) -> bool:
    pass

# IMGUI_API bool              IsMouseDoubleClicked(ImGuiMouseButton button, ImGuiID owner_id);    /* original C++ signature */
def is_mouse_double_clicked(button: MouseButton, owner_id: ID) -> bool:
    pass

# [EXPERIMENTAL] Shortcut Routing
# - ImGuiKeyChord = a ImGuiKey optionally OR-red with ImGuiMod_Alt/ImGuiMod_Ctrl/ImGuiMod_Shift/ImGuiMod_Super.
#     ImGuiKey_C                 (accepted by functions taking ImGuiKey or ImGuiKeyChord)
#     ImGuiKey_C | ImGuiMod_Ctrl (accepted by functions taking ImGuiKeyChord)
#   ONLY ImGuiMod_XXX values are legal to 'OR' with an ImGuiKey. You CANNOT 'OR' two ImGuiKey values.
# - When using one of the routing flags (e.g. ImGuiInputFlags_RouteFocused): routes requested ahead of time given a chord (key + modifiers) and a routing policy.
# - Routes are resolved during NewFrame(): if keyboard modifiers are matching current ones: SetKeyOwner() is called + route is granted for the frame.
# - Route is granted to a single owner. When multiple requests are made we have policies to select the winning route.
# - Multiple read sites may use the same owner id and will all get the granted route.
# - For routing: when owner_id is 0 we use the current Focus Scope ID as a default owner in order to identify our location.
# - TL;DR;
#   - IsKeyChordPressed() compares mods + call IsKeyPressed() -> function has no side-effect.
#   - Shortcut() submits a route then if currently can be routed calls IsKeyChordPressed() -> function has (desirable) side-effects.
# IMGUI_API bool              IsKeyChordPressed(ImGuiKeyChord key_chord, ImGuiID owner_id, ImGuiInputFlags flags = 0);    /* original C++ signature */
def is_key_chord_pressed(
    key_chord: KeyChord, owner_id: ID, flags: InputFlags = 0
) -> bool:
    pass

# IMGUI_API bool              Shortcut(ImGuiKeyChord key_chord, ImGuiID owner_id = 0, ImGuiInputFlags flags = 0);    /* original C++ signature */
def shortcut(key_chord: KeyChord, owner_id: ID = 0, flags: InputFlags = 0) -> bool:
    pass

# IMGUI_API bool              SetShortcutRouting(ImGuiKeyChord key_chord, ImGuiID owner_id = 0, ImGuiInputFlags flags = 0);    /* original C++ signature */
def set_shortcut_routing(
    key_chord: KeyChord, owner_id: ID = 0, flags: InputFlags = 0
) -> bool:
    pass

# IMGUI_API bool              TestShortcutRouting(ImGuiKeyChord key_chord, ImGuiID owner_id);    /* original C++ signature */
def test_shortcut_routing(key_chord: KeyChord, owner_id: ID) -> bool:
    pass

# IMGUI_API ImGuiKeyRoutingData* GetShortcutRoutingData(ImGuiKeyChord key_chord);    /* original C++ signature */
def get_shortcut_routing_data(key_chord: KeyChord) -> KeyRoutingData:
    pass

# Docking
# (some functions are only declared in imgui.cpp, see Docking section)
# IMGUI_API void          DockContextInitialize(ImGuiContext* ctx);    /* original C++ signature */
def dock_context_initialize(ctx: Context) -> None:
    pass

# IMGUI_API void          DockContextShutdown(ImGuiContext* ctx);    /* original C++ signature */
def dock_context_shutdown(ctx: Context) -> None:
    pass

# IMGUI_API void          DockContextClearNodes(ImGuiContext* ctx, ImGuiID root_id, bool clear_settings_refs);     /* original C++ signature */
def dock_context_clear_nodes(
    ctx: Context, root_id: ID, clear_settings_refs: bool
) -> None:
    """Use root_id==0 to clear all"""
    pass

# IMGUI_API void          DockContextRebuildNodes(ImGuiContext* ctx);    /* original C++ signature */
def dock_context_rebuild_nodes(ctx: Context) -> None:
    pass

# IMGUI_API void          DockContextNewFrameUpdateUndocking(ImGuiContext* ctx);    /* original C++ signature */
def dock_context_new_frame_update_undocking(ctx: Context) -> None:
    pass

# IMGUI_API void          DockContextNewFrameUpdateDocking(ImGuiContext* ctx);    /* original C++ signature */
def dock_context_new_frame_update_docking(ctx: Context) -> None:
    pass

# IMGUI_API void          DockContextEndFrame(ImGuiContext* ctx);    /* original C++ signature */
def dock_context_end_frame(ctx: Context) -> None:
    pass

# IMGUI_API ImGuiID       DockContextGenNodeID(ImGuiContext* ctx);    /* original C++ signature */
def dock_context_gen_node_id(ctx: Context) -> ID:
    pass

# IMGUI_API void          DockContextQueueDock(ImGuiContext* ctx, ImGuiWindow* target, ImGuiDockNode* target_node, ImGuiWindow* payload, ImGuiDir split_dir, float split_ratio, bool split_outer);    /* original C++ signature */
def dock_context_queue_dock(
    ctx: Context,
    target: Window,
    target_node: DockNode,
    payload: Window,
    split_dir: Dir,
    split_ratio: float,
    split_outer: bool,
) -> None:
    pass

# IMGUI_API void          DockContextQueueUndockWindow(ImGuiContext* ctx, ImGuiWindow* window);    /* original C++ signature */
def dock_context_queue_undock_window(ctx: Context, window: Window) -> None:
    pass

# IMGUI_API void          DockContextQueueUndockNode(ImGuiContext* ctx, ImGuiDockNode* node);    /* original C++ signature */
def dock_context_queue_undock_node(ctx: Context, node: DockNode) -> None:
    pass

# IMGUI_API void          DockContextProcessUndockWindow(ImGuiContext* ctx, ImGuiWindow* window, bool clear_persistent_docking_ref = true);    /* original C++ signature */
def dock_context_process_undock_window(
    ctx: Context, window: Window, clear_persistent_docking_ref: bool = True
) -> None:
    pass

# IMGUI_API void          DockContextProcessUndockNode(ImGuiContext* ctx, ImGuiDockNode* node);    /* original C++ signature */
def dock_context_process_undock_node(ctx: Context, node: DockNode) -> None:
    pass

# IMGUI_API bool          DockContextCalcDropPosForDocking(ImGuiWindow* target, ImGuiDockNode* target_node, ImGuiWindow* payload_window, ImGuiDockNode* payload_node, ImGuiDir split_dir, bool split_outer, ImVec2* out_pos);    /* original C++ signature */
def dock_context_calc_drop_pos_for_docking(
    target: Window,
    target_node: DockNode,
    payload_window: Window,
    payload_node: DockNode,
    split_dir: Dir,
    split_outer: bool,
    out_pos: ImVec2,
) -> bool:
    pass

# IMGUI_API ImGuiDockNode*DockContextFindNodeByID(ImGuiContext* ctx, ImGuiID id);    /* original C++ signature */
def dock_context_find_node_by_id(ctx: Context, id_: ID) -> DockNode:
    pass

# IMGUI_API void          DockNodeWindowMenuHandler_Default(ImGuiContext* ctx, ImGuiDockNode* node, ImGuiTabBar* tab_bar);    /* original C++ signature */
def dock_node_window_menu_handler_default(
    ctx: Context, node: DockNode, tab_bar: TabBar
) -> None:
    pass

# IMGUI_API bool          DockNodeBeginAmendTabBar(ImGuiDockNode* node);    /* original C++ signature */
def dock_node_begin_amend_tab_bar(node: DockNode) -> bool:
    pass

# IMGUI_API void          DockNodeEndAmendTabBar();    /* original C++ signature */
def dock_node_end_amend_tab_bar() -> None:
    pass

# inline ImGuiDockNode*   DockNodeGetRootNode(ImGuiDockNode* node)                 { while (node->ParentNode) node = node->ParentNode; return node; }    /* original C++ signature */
def dock_node_get_root_node(node: DockNode) -> DockNode:
    """(private API)"""
    pass

# inline bool             DockNodeIsInHierarchyOf(ImGuiDockNode* node, ImGuiDockNode* parent) { while (node) { if (node == parent) return true; node = node->ParentNode; } return false; }    /* original C++ signature */
def dock_node_is_in_hierarchy_of(node: DockNode, parent: DockNode) -> bool:
    """(private API)"""
    pass

# inline int              DockNodeGetDepth(const ImGuiDockNode* node)              { int depth = 0; while (node->ParentNode) { node = node->ParentNode; depth++; } return depth; }    /* original C++ signature */
def dock_node_get_depth(node: DockNode) -> int:
    """(private API)"""
    pass

# inline ImGuiID          DockNodeGetWindowMenuButtonId(const ImGuiDockNode* node) { return ImHashStr("#COLLAPSE", 0, node->ID); }    /* original C++ signature */
def dock_node_get_window_menu_button_id(node: DockNode) -> ID:
    """(private API)"""
    pass

# inline ImGuiDockNode*   GetWindowDockNode()                                      { ImGuiContext& g = *GImGui; return g.CurrentWindow->DockNode; }    /* original C++ signature */
def get_window_dock_node() -> DockNode:
    """(private API)"""
    pass

# IMGUI_API bool          GetWindowAlwaysWantOwnTabBar(ImGuiWindow* window);    /* original C++ signature */
def get_window_always_want_own_tab_bar(window: Window) -> bool:
    pass

# IMGUI_API void          BeginDocked(ImGuiWindow* window, bool* p_open);    /* original C++ signature */
def begin_docked(window: Window, p_open: bool) -> bool:
    pass

# IMGUI_API void          BeginDockableDragDropSource(ImGuiWindow* window);    /* original C++ signature */
def begin_dockable_drag_drop_source(window: Window) -> None:
    pass

# IMGUI_API void          BeginDockableDragDropTarget(ImGuiWindow* window);    /* original C++ signature */
def begin_dockable_drag_drop_target(window: Window) -> None:
    pass

# IMGUI_API void          SetWindowDock(ImGuiWindow* window, ImGuiID dock_id, ImGuiCond cond);    /* original C++ signature */
def set_window_dock(window: Window, dock_id: ID, cond: Cond) -> None:
    pass

# Docking - Builder function needs to be generally called before the node is used/submitted.
# - The DockBuilderXXX functions are designed to _eventually_ become a public API, but it is too early to expose it and guarantee stability.
# - Do not hold on ImGuiDockNode* pointers! They may be invalidated by any split/merge/remove operation and every frame.
# - To create a DockSpace() node, make sure to set the ImGuiDockNodeFlags_DockSpace flag when calling DockBuilderAddNode().
#   You can create dockspace nodes (attached to a window) _or_ floating nodes (carry its own window) with this API.
# - DockBuilderSplitNode() create 2 child nodes within 1 node. The initial node becomes a parent node.
# - If you intend to split the node immediately after creation using DockBuilderSplitNode(), make sure
#   to call DockBuilderSetNodeSize() beforehand. If you don't, the resulting split sizes may not be reliable.
# - Call DockBuilderFinish() after you are done.
# IMGUI_API void          DockBuilderDockWindow(const char* window_name, ImGuiID node_id);    /* original C++ signature */
def dock_builder_dock_window(window_name: str, node_id: ID) -> None:
    pass

# IMGUI_API ImGuiDockNode*DockBuilderGetNode(ImGuiID node_id);    /* original C++ signature */
def dock_builder_get_node(node_id: ID) -> DockNode:
    pass

# inline ImGuiDockNode*   DockBuilderGetCentralNode(ImGuiID node_id)              { ImGuiDockNode* node = DockBuilderGetNode(node_id); if (!node) return NULL; return DockNodeGetRootNode(node)->CentralNode; }    /* original C++ signature */
def dock_builder_get_central_node(node_id: ID) -> DockNode:
    """(private API)"""
    pass

# IMGUI_API ImGuiID       DockBuilderAddNode(ImGuiID node_id = 0, ImGuiDockNodeFlags flags = 0);    /* original C++ signature */
def dock_builder_add_node(node_id: ID = 0, flags: DockNodeFlags = 0) -> ID:
    pass

# IMGUI_API void          DockBuilderRemoveNode(ImGuiID node_id);                     /* original C++ signature */
def dock_builder_remove_node(node_id: ID) -> None:
    """Remove node and all its child, undock all windows"""
    pass

# IMGUI_API void          DockBuilderRemoveNodeDockedWindows(ImGuiID node_id, bool clear_settings_refs = true);    /* original C++ signature */
def dock_builder_remove_node_docked_windows(
    node_id: ID, clear_settings_refs: bool = True
) -> None:
    pass

# IMGUI_API void          DockBuilderRemoveNodeChildNodes(ImGuiID node_id);           /* original C++ signature */
def dock_builder_remove_node_child_nodes(node_id: ID) -> None:
    """Remove all split/hierarchy. All remaining docked windows will be re-docked to the remaining root node (node_id)."""
    pass

# IMGUI_API void          DockBuilderSetNodePos(ImGuiID node_id, ImVec2 pos);    /* original C++ signature */
def dock_builder_set_node_pos(node_id: ID, pos: ImVec2) -> None:
    pass

# IMGUI_API void          DockBuilderSetNodeSize(ImGuiID node_id, ImVec2 size);    /* original C++ signature */
def dock_builder_set_node_size(node_id: ID, size: ImVec2) -> None:
    pass

# IMGUI_API void          DockBuilderCopyNode(ImGuiID src_node_id, ImGuiID dst_node_id, ImVector<ImGuiID>* out_node_remap_pairs);    /* original C++ signature */
def dock_builder_copy_node(
    src_node_id: ID, dst_node_id: ID, out_node_remap_pairs: ImVector_ID
) -> None:
    pass

# IMGUI_API void          DockBuilderCopyWindowSettings(const char* src_name, const char* dst_name);    /* original C++ signature */
def dock_builder_copy_window_settings(src_name: str, dst_name: str) -> None:
    pass

# IMGUI_API void          DockBuilderFinish(ImGuiID node_id);    /* original C++ signature */
def dock_builder_finish(node_id: ID) -> None:
    pass

# [EXPERIMENTAL] Focus Scope
# This is generally used to identify a unique input location (for e.g. a selection set)
# There is one per window (automatically set in Begin), but:
# - Selection patterns generally need to react (e.g. clear a selection) when landing on one item of the set.
#   So in order to identify a set multiple lists in same window may each need a focus scope.
#   If you imagine an hypothetical BeginSelectionGroup()/EndSelectionGroup() api, it would likely call PushFocusScope()/EndFocusScope()
# - Shortcut routing also use focus scope as a default location identifier if an owner is not provided.
# We don't use the ID Stack for this as it is common to want them separate.
# IMGUI_API void          PushFocusScope(ImGuiID id);    /* original C++ signature */
def push_focus_scope(id_: ID) -> None:
    pass

# IMGUI_API void          PopFocusScope();    /* original C++ signature */
def pop_focus_scope() -> None:
    pass

# inline ImGuiID          GetCurrentFocusScope() { ImGuiContext& g = *GImGui; return g.CurrentFocusScopeId; }       /* original C++ signature */
def get_current_focus_scope() -> ID:
    """(private API)

    Focus scope we are outputting into, set by PushFocusScope()
    """
    pass

# Drag and Drop
# IMGUI_API bool          IsDragDropActive();    /* original C++ signature */
def is_drag_drop_active() -> bool:
    pass

# IMGUI_API bool          BeginDragDropTargetCustom(const ImRect& bb, ImGuiID id);    /* original C++ signature */
def begin_drag_drop_target_custom(bb: ImRect, id_: ID) -> bool:
    pass

# IMGUI_API void          ClearDragDrop();    /* original C++ signature */
def clear_drag_drop() -> None:
    pass

# IMGUI_API bool          IsDragDropPayloadBeingAccepted();    /* original C++ signature */
def is_drag_drop_payload_being_accepted() -> bool:
    pass

# IMGUI_API void          RenderDragDropTargetRect(const ImRect& bb);    /* original C++ signature */
def render_drag_drop_target_rect(bb: ImRect) -> None:
    pass

# Typing-Select API
# IMGUI_API ImGuiTypingSelectRequest* GetTypingSelectRequest(ImGuiTypingSelectFlags flags = ImGuiTypingSelectFlags_None);    /* original C++ signature */
def get_typing_select_request(
    flags: TypingSelectFlags = TypingSelectFlags_None,
) -> TypingSelectRequest:
    pass

# Internal Columns API (this is not exposed because we will encourage transitioning to the Tables API)
# IMGUI_API void          SetWindowClipRectBeforeSetChannel(ImGuiWindow* window, const ImRect& clip_rect);    /* original C++ signature */
def set_window_clip_rect_before_set_channel(window: Window, clip_rect: ImRect) -> None:
    pass

# IMGUI_API void          BeginColumns(const char* str_id, int count, ImGuiOldColumnFlags flags = 0);     /* original C++ signature */
def begin_columns(str_id: str, count: int, flags: OldColumnFlags = 0) -> None:
    """setup number of columns. use an identifier to distinguish multiple column sets. close with EndColumns()."""
    pass

# IMGUI_API void          EndColumns();                                                                   /* original C++ signature */
def end_columns() -> None:
    """close columns"""
    pass

# IMGUI_API void          PushColumnClipRect(int column_index);    /* original C++ signature */
def push_column_clip_rect(column_index: int) -> None:
    pass

# IMGUI_API void          PushColumnsBackground();    /* original C++ signature */
def push_columns_background() -> None:
    pass

# IMGUI_API void          PopColumnsBackground();    /* original C++ signature */
def pop_columns_background() -> None:
    pass

# IMGUI_API ImGuiID       GetColumnsID(const char* str_id, int count);    /* original C++ signature */
def get_columns_id(str_id: str, count: int) -> ID:
    pass

# IMGUI_API ImGuiOldColumns* FindOrCreateColumns(ImGuiWindow* window, ImGuiID id);    /* original C++ signature */
def find_or_create_columns(window: Window, id_: ID) -> OldColumns:
    pass

# IMGUI_API float         GetColumnOffsetFromNorm(const ImGuiOldColumns* columns, float offset_norm);    /* original C++ signature */
def get_column_offset_from_norm(columns: OldColumns, offset_norm: float) -> float:
    pass

# IMGUI_API float         GetColumnNormFromOffset(const ImGuiOldColumns* columns, float offset);    /* original C++ signature */
def get_column_norm_from_offset(columns: OldColumns, offset: float) -> float:
    pass

# Tables: Candidates for public API
# IMGUI_API void          TableOpenContextMenu(int column_n = -1);    /* original C++ signature */
def table_open_context_menu(column_n: int = -1) -> None:
    pass

# IMGUI_API void          TableSetColumnWidth(int column_n, float width);    /* original C++ signature */
def table_set_column_width(column_n: int, width: float) -> None:
    pass

# IMGUI_API void          TableSetColumnSortDirection(int column_n, ImGuiSortDirection sort_direction, bool append_to_sort_specs);    /* original C++ signature */
def table_set_column_sort_direction(
    column_n: int, sort_direction: SortDirection, append_to_sort_specs: bool
) -> None:
    pass

# IMGUI_API int           TableGetHoveredColumn();        /* original C++ signature */
def table_get_hovered_column() -> int:
    """May use (TableGetColumnFlags() & ImGuiTableColumnFlags_IsHovered) instead. Return hovered column. return -1 when table is not hovered. return columns_count if the unused space at the right of visible columns is hovered."""
    pass

# IMGUI_API int           TableGetHoveredRow();           /* original C++ signature */
def table_get_hovered_row() -> int:
    """Retrieve *PREVIOUS FRAME* hovered row. This difference with TableGetHoveredColumn() is the reason why this is not public yet."""
    pass

# IMGUI_API float         TableGetHeaderRowHeight();    /* original C++ signature */
def table_get_header_row_height() -> float:
    pass

# IMGUI_API float         TableGetHeaderAngledMaxLabelWidth();    /* original C++ signature */
def table_get_header_angled_max_label_width() -> float:
    pass

# IMGUI_API void          TablePushBackgroundChannel();    /* original C++ signature */
def table_push_background_channel() -> None:
    pass

# IMGUI_API void          TablePopBackgroundChannel();    /* original C++ signature */
def table_pop_background_channel() -> None:
    pass

# IMGUI_API void          TableAngledHeadersRowEx(float angle, float label_width = 0.0f);    /* original C++ signature */
def table_angled_headers_row_ex(angle: float, label_width: float = 0.0) -> None:
    pass

# inline    ImGuiTable*   GetCurrentTable() { ImGuiContext& g = *GImGui; return g.CurrentTable; }    /* original C++ signature */
def get_current_table() -> Table:
    """Tables: Internals
    (private API)
    """
    pass

# IMGUI_API ImGuiTable*   TableFindByID(ImGuiID id);    /* original C++ signature */
def table_find_by_id(id_: ID) -> Table:
    pass

# IMGUI_API bool          BeginTableEx(const char* name, ImGuiID id, int columns_count, ImGuiTableFlags flags = 0, const ImVec2& outer_size = ImVec2(0, 0), float inner_width = 0.0f);    /* original C++ signature */
def begin_table_ex(
    name: str,
    id_: ID,
    columns_count: int,
    flags: TableFlags = 0,
    outer_size: ImVec2 = ImVec2(0, 0),
    inner_width: float = 0.0,
) -> bool:
    pass

# IMGUI_API void          TableBeginInitMemory(ImGuiTable* table, int columns_count);    /* original C++ signature */
def table_begin_init_memory(table: Table, columns_count: int) -> None:
    pass

# IMGUI_API void          TableBeginApplyRequests(ImGuiTable* table);    /* original C++ signature */
def table_begin_apply_requests(table: Table) -> None:
    pass

# IMGUI_API void          TableSetupDrawChannels(ImGuiTable* table);    /* original C++ signature */
def table_setup_draw_channels(table: Table) -> None:
    pass

# IMGUI_API void          TableUpdateLayout(ImGuiTable* table);    /* original C++ signature */
def table_update_layout(table: Table) -> None:
    pass

# IMGUI_API void          TableUpdateBorders(ImGuiTable* table);    /* original C++ signature */
def table_update_borders(table: Table) -> None:
    pass

# IMGUI_API void          TableUpdateColumnsWeightFromWidth(ImGuiTable* table);    /* original C++ signature */
def table_update_columns_weight_from_width(table: Table) -> None:
    pass

# IMGUI_API void          TableDrawBorders(ImGuiTable* table);    /* original C++ signature */
def table_draw_borders(table: Table) -> None:
    pass

# IMGUI_API void          TableDrawDefaultContextMenu(ImGuiTable* table, ImGuiTableFlags flags_for_section_to_display);    /* original C++ signature */
def table_draw_default_context_menu(
    table: Table, flags_for_section_to_display: TableFlags
) -> None:
    pass

# IMGUI_API bool          TableBeginContextMenuPopup(ImGuiTable* table);    /* original C++ signature */
def table_begin_context_menu_popup(table: Table) -> bool:
    pass

# IMGUI_API void          TableMergeDrawChannels(ImGuiTable* table);    /* original C++ signature */
def table_merge_draw_channels(table: Table) -> None:
    pass

# inline ImGuiTableInstanceData*  TableGetInstanceData(ImGuiTable* table, int instance_no) { if (instance_no == 0) return &table->InstanceDataFirst; return &table->InstanceDataExtra[instance_no - 1]; }    /* original C++ signature */
def table_get_instance_data(table: Table, instance_no: int) -> TableInstanceData:
    """(private API)"""
    pass

# inline ImGuiID                  TableGetInstanceID(ImGuiTable* table, int instance_no)   { return TableGetInstanceData(table, instance_no)->TableInstanceID; }    /* original C++ signature */
def table_get_instance_id(table: Table, instance_no: int) -> ID:
    """(private API)"""
    pass

# IMGUI_API void          TableSortSpecsSanitize(ImGuiTable* table);    /* original C++ signature */
def table_sort_specs_sanitize(table: Table) -> None:
    pass

# IMGUI_API void          TableSortSpecsBuild(ImGuiTable* table);    /* original C++ signature */
def table_sort_specs_build(table: Table) -> None:
    pass

# IMGUI_API ImGuiSortDirection TableGetColumnNextSortDirection(ImGuiTableColumn* column);    /* original C++ signature */
def table_get_column_next_sort_direction(column: TableColumn) -> SortDirection:
    pass

# IMGUI_API void          TableFixColumnSortDirection(ImGuiTable* table, ImGuiTableColumn* column);    /* original C++ signature */
def table_fix_column_sort_direction(table: Table, column: TableColumn) -> None:
    pass

# IMGUI_API float         TableGetColumnWidthAuto(ImGuiTable* table, ImGuiTableColumn* column);    /* original C++ signature */
def table_get_column_width_auto(table: Table, column: TableColumn) -> float:
    pass

# IMGUI_API void          TableBeginRow(ImGuiTable* table);    /* original C++ signature */
def table_begin_row(table: Table) -> None:
    pass

# IMGUI_API void          TableEndRow(ImGuiTable* table);    /* original C++ signature */
def table_end_row(table: Table) -> None:
    pass

# IMGUI_API void          TableBeginCell(ImGuiTable* table, int column_n);    /* original C++ signature */
def table_begin_cell(table: Table, column_n: int) -> None:
    pass

# IMGUI_API void          TableEndCell(ImGuiTable* table);    /* original C++ signature */
def table_end_cell(table: Table) -> None:
    pass

# IMGUI_API ImRect        TableGetCellBgRect(const ImGuiTable* table, int column_n);    /* original C++ signature */
def table_get_cell_bg_rect(table: Table, column_n: int) -> ImRect:
    pass

# IMGUI_API const char*   TableGetColumnName(const ImGuiTable* table, int column_n);    /* original C++ signature */
def table_get_column_name(table: Table, column_n: int) -> str:
    pass

# IMGUI_API ImGuiID       TableGetColumnResizeID(ImGuiTable* table, int column_n, int instance_no = 0);    /* original C++ signature */
def table_get_column_resize_id(table: Table, column_n: int, instance_no: int = 0) -> ID:
    pass

# IMGUI_API float         TableGetMaxColumnWidth(const ImGuiTable* table, int column_n);    /* original C++ signature */
def table_get_max_column_width(table: Table, column_n: int) -> float:
    pass

# IMGUI_API void          TableSetColumnWidthAutoSingle(ImGuiTable* table, int column_n);    /* original C++ signature */
def table_set_column_width_auto_single(table: Table, column_n: int) -> None:
    pass

# IMGUI_API void          TableSetColumnWidthAutoAll(ImGuiTable* table);    /* original C++ signature */
def table_set_column_width_auto_all(table: Table) -> None:
    pass

# IMGUI_API void          TableRemove(ImGuiTable* table);    /* original C++ signature */
def table_remove(table: Table) -> None:
    pass

# IMGUI_API void          TableGcCompactTransientBuffers(ImGuiTable* table);    /* original C++ signature */
@overload
def table_gc_compact_transient_buffers(table: Table) -> None:
    pass

# IMGUI_API void          TableGcCompactTransientBuffers(ImGuiTableTempData* table);    /* original C++ signature */
@overload
def table_gc_compact_transient_buffers(table: TableTempData) -> None:
    pass

# IMGUI_API void          TableGcCompactSettings();    /* original C++ signature */
def table_gc_compact_settings() -> None:
    pass

# Tables: Settings
# IMGUI_API void                  TableLoadSettings(ImGuiTable* table);    /* original C++ signature */
def table_load_settings(table: Table) -> None:
    pass

# IMGUI_API void                  TableSaveSettings(ImGuiTable* table);    /* original C++ signature */
def table_save_settings(table: Table) -> None:
    pass

# IMGUI_API void                  TableResetSettings(ImGuiTable* table);    /* original C++ signature */
def table_reset_settings(table: Table) -> None:
    pass

# IMGUI_API ImGuiTableSettings*   TableGetBoundSettings(ImGuiTable* table);    /* original C++ signature */
def table_get_bound_settings(table: Table) -> TableSettings:
    pass

# IMGUI_API void                  TableSettingsAddSettingsHandler();    /* original C++ signature */
def table_settings_add_settings_handler() -> None:
    pass

# IMGUI_API ImGuiTableSettings*   TableSettingsCreate(ImGuiID id, int columns_count);    /* original C++ signature */
def table_settings_create(id_: ID, columns_count: int) -> TableSettings:
    pass

# IMGUI_API ImGuiTableSettings*   TableSettingsFindByID(ImGuiID id);    /* original C++ signature */
def table_settings_find_by_id(id_: ID) -> TableSettings:
    pass

# inline    ImGuiTabBar*  GetCurrentTabBar() { ImGuiContext& g = *GImGui; return g.CurrentTabBar; }    /* original C++ signature */
def get_current_tab_bar() -> TabBar:
    """Tab Bars
    (private API)
    """
    pass

# IMGUI_API bool          BeginTabBarEx(ImGuiTabBar* tab_bar, const ImRect& bb, ImGuiTabBarFlags flags);    /* original C++ signature */
def begin_tab_bar_ex(tab_bar: TabBar, bb: ImRect, flags: TabBarFlags) -> bool:
    pass

# IMGUI_API ImGuiTabItem* TabBarFindTabByID(ImGuiTabBar* tab_bar, ImGuiID tab_id);    /* original C++ signature */
def tab_bar_find_tab_by_id(tab_bar: TabBar, tab_id: ID) -> TabItem:
    pass

# IMGUI_API ImGuiTabItem* TabBarFindTabByOrder(ImGuiTabBar* tab_bar, int order);    /* original C++ signature */
def tab_bar_find_tab_by_order(tab_bar: TabBar, order: int) -> TabItem:
    pass

# IMGUI_API ImGuiTabItem* TabBarFindMostRecentlySelectedTabForActiveWindow(ImGuiTabBar* tab_bar);    /* original C++ signature */
def tab_bar_find_most_recently_selected_tab_for_active_window(
    tab_bar: TabBar,
) -> TabItem:
    pass

# IMGUI_API ImGuiTabItem* TabBarGetCurrentTab(ImGuiTabBar* tab_bar);    /* original C++ signature */
def tab_bar_get_current_tab(tab_bar: TabBar) -> TabItem:
    pass

# inline int              TabBarGetTabOrder(ImGuiTabBar* tab_bar, ImGuiTabItem* tab) { return tab_bar->Tabs.index_from_ptr(tab); }    /* original C++ signature */
def tab_bar_get_tab_order(tab_bar: TabBar, tab: TabItem) -> int:
    """(private API)"""
    pass

# IMGUI_API const char*   TabBarGetTabName(ImGuiTabBar* tab_bar, ImGuiTabItem* tab);    /* original C++ signature */
def tab_bar_get_tab_name(tab_bar: TabBar, tab: TabItem) -> str:
    pass

# IMGUI_API void          TabBarAddTab(ImGuiTabBar* tab_bar, ImGuiTabItemFlags tab_flags, ImGuiWindow* window);    /* original C++ signature */
def tab_bar_add_tab(tab_bar: TabBar, tab_flags: TabItemFlags, window: Window) -> None:
    pass

# IMGUI_API void          TabBarRemoveTab(ImGuiTabBar* tab_bar, ImGuiID tab_id);    /* original C++ signature */
def tab_bar_remove_tab(tab_bar: TabBar, tab_id: ID) -> None:
    pass

# IMGUI_API void          TabBarCloseTab(ImGuiTabBar* tab_bar, ImGuiTabItem* tab);    /* original C++ signature */
def tab_bar_close_tab(tab_bar: TabBar, tab: TabItem) -> None:
    pass

# IMGUI_API void          TabBarQueueFocus(ImGuiTabBar* tab_bar, ImGuiTabItem* tab);    /* original C++ signature */
def tab_bar_queue_focus(tab_bar: TabBar, tab: TabItem) -> None:
    pass

# IMGUI_API void          TabBarQueueReorder(ImGuiTabBar* tab_bar, ImGuiTabItem* tab, int offset);    /* original C++ signature */
def tab_bar_queue_reorder(tab_bar: TabBar, tab: TabItem, offset: int) -> None:
    pass

# IMGUI_API void          TabBarQueueReorderFromMousePos(ImGuiTabBar* tab_bar, ImGuiTabItem* tab, ImVec2 mouse_pos);    /* original C++ signature */
def tab_bar_queue_reorder_from_mouse_pos(
    tab_bar: TabBar, tab: TabItem, mouse_pos: ImVec2
) -> None:
    pass

# IMGUI_API bool          TabBarProcessReorder(ImGuiTabBar* tab_bar);    /* original C++ signature */
def tab_bar_process_reorder(tab_bar: TabBar) -> bool:
    pass

# IMGUI_API bool          TabItemEx(ImGuiTabBar* tab_bar, const char* label, bool* p_open, ImGuiTabItemFlags flags, ImGuiWindow* docked_window);    /* original C++ signature */
def tab_item_ex(
    tab_bar: TabBar,
    label: str,
    p_open: bool,
    flags: TabItemFlags,
    docked_window: Window,
) -> Tuple[bool, bool]:
    pass

# IMGUI_API ImVec2        TabItemCalcSize(const char* label, bool has_close_button_or_unsaved_marker);    /* original C++ signature */
@overload
def tab_item_calc_size(label: str, has_close_button_or_unsaved_marker: bool) -> ImVec2:
    pass

# IMGUI_API ImVec2        TabItemCalcSize(ImGuiWindow* window);    /* original C++ signature */
@overload
def tab_item_calc_size(window: Window) -> ImVec2:
    pass

# IMGUI_API void          TabItemBackground(ImDrawList* draw_list, const ImRect& bb, ImGuiTabItemFlags flags, ImU32 col);    /* original C++ signature */
def tab_item_background(
    draw_list: ImDrawList, bb: ImRect, flags: TabItemFlags, col: ImU32
) -> None:
    pass

# IMGUI_API void          TabItemLabelAndCloseButton(ImDrawList* draw_list, const ImRect& bb, ImGuiTabItemFlags flags, ImVec2 frame_padding, const char* label, ImGuiID tab_id, ImGuiID close_button_id, bool is_contents_visible, bool* out_just_closed, bool* out_text_clipped);    /* original C++ signature */
def tab_item_label_and_close_button(
    draw_list: ImDrawList,
    bb: ImRect,
    flags: TabItemFlags,
    frame_padding: ImVec2,
    label: str,
    tab_id: ID,
    close_button_id: ID,
    is_contents_visible: bool,
    out_just_closed: bool,
    out_text_clipped: bool,
) -> Tuple[bool, bool]:
    pass

# Render helpers
# AVOID USING OUTSIDE OF IMGUI.CPP! NOT FOR PUBLIC CONSUMPTION. THOSE FUNCTIONS ARE A MESS. THEIR SIGNATURE AND BEHAVIOR WILL CHANGE, THEY NEED TO BE REFACTORED INTO SOMETHING DECENT.
# NB: All position are in absolute pixels coordinates (we are never using window coordinates internally)
# IMGUI_API void          RenderText(ImVec2 pos, const char* text, const char* text_end = NULL, bool hide_text_after_hash = true);    /* original C++ signature */
def render_text(
    pos: ImVec2,
    text: str,
    text_end: Optional[str] = None,
    hide_text_after_hash: bool = True,
) -> None:
    pass

# IMGUI_API void          RenderTextWrapped(ImVec2 pos, const char* text, const char* text_end, float wrap_width);    /* original C++ signature */
def render_text_wrapped(
    pos: ImVec2, text: str, text_end: str, wrap_width: float
) -> None:
    pass

# IMGUI_API void          RenderTextClipped(const ImVec2& pos_min, const ImVec2& pos_max, const char* text, const char* text_end, const ImVec2* text_size_if_known, const ImVec2& align = ImVec2(0, 0), const ImRect* clip_rect = NULL);    /* original C++ signature */
def render_text_clipped(
    pos_min: ImVec2,
    pos_max: ImVec2,
    text: str,
    text_end: str,
    text_size_if_known: ImVec2,
    align: ImVec2 = ImVec2(0, 0),
    clip_rect: Optional[ImRect] = None,
) -> None:
    pass

# IMGUI_API void          RenderTextClippedEx(ImDrawList* draw_list, const ImVec2& pos_min, const ImVec2& pos_max, const char* text, const char* text_end, const ImVec2* text_size_if_known, const ImVec2& align = ImVec2(0, 0), const ImRect* clip_rect = NULL);    /* original C++ signature */
def render_text_clipped_ex(
    draw_list: ImDrawList,
    pos_min: ImVec2,
    pos_max: ImVec2,
    text: str,
    text_end: str,
    text_size_if_known: ImVec2,
    align: ImVec2 = ImVec2(0, 0),
    clip_rect: Optional[ImRect] = None,
) -> None:
    pass

# IMGUI_API void          RenderTextEllipsis(ImDrawList* draw_list, const ImVec2& pos_min, const ImVec2& pos_max, float clip_max_x, float ellipsis_max_x, const char* text, const char* text_end, const ImVec2* text_size_if_known);    /* original C++ signature */
def render_text_ellipsis(
    draw_list: ImDrawList,
    pos_min: ImVec2,
    pos_max: ImVec2,
    clip_max_x: float,
    ellipsis_max_x: float,
    text: str,
    text_end: str,
    text_size_if_known: ImVec2,
) -> None:
    pass

# IMGUI_API void          RenderFrame(ImVec2 p_min, ImVec2 p_max, ImU32 fill_col, bool border = true, float rounding = 0.0f);    /* original C++ signature */
def render_frame(
    p_min: ImVec2,
    p_max: ImVec2,
    fill_col: ImU32,
    border: bool = True,
    rounding: float = 0.0,
) -> None:
    pass

# IMGUI_API void          RenderFrameBorder(ImVec2 p_min, ImVec2 p_max, float rounding = 0.0f);    /* original C++ signature */
def render_frame_border(p_min: ImVec2, p_max: ImVec2, rounding: float = 0.0) -> None:
    pass

# IMGUI_API void          RenderColorRectWithAlphaCheckerboard(ImDrawList* draw_list, ImVec2 p_min, ImVec2 p_max, ImU32 fill_col, float grid_step, ImVec2 grid_off, float rounding = 0.0f, ImDrawFlags flags = 0);    /* original C++ signature */
def render_color_rect_with_alpha_checkerboard(
    draw_list: ImDrawList,
    p_min: ImVec2,
    p_max: ImVec2,
    fill_col: ImU32,
    grid_step: float,
    grid_off: ImVec2,
    rounding: float = 0.0,
    flags: ImDrawFlags = 0,
) -> None:
    pass

# IMGUI_API void          RenderNavHighlight(const ImRect& bb, ImGuiID id, ImGuiNavHighlightFlags flags = ImGuiNavHighlightFlags_TypeDefault);     /* original C++ signature */
def render_nav_highlight(
    bb: ImRect, id_: ID, flags: NavHighlightFlags = NavHighlightFlags_TypeDefault
) -> None:
    """Navigation highlight"""
    pass

# IMGUI_API const char*   FindRenderedTextEnd(const char* text, const char* text_end = NULL);     /* original C++ signature */
def find_rendered_text_end(text: str, text_end: Optional[str] = None) -> str:
    """Find the optional ## from which we stop displaying text."""
    pass

# IMGUI_API void          RenderMouseCursor(ImVec2 pos, float scale, ImGuiMouseCursor mouse_cursor, ImU32 col_fill, ImU32 col_border, ImU32 col_shadow);    /* original C++ signature */
def render_mouse_cursor(
    pos: ImVec2,
    scale: float,
    mouse_cursor: MouseCursor,
    col_fill: ImU32,
    col_border: ImU32,
    col_shadow: ImU32,
) -> None:
    pass

# Render helpers (those functions don't access any ImGui state!)
# IMGUI_API void          RenderArrow(ImDrawList* draw_list, ImVec2 pos, ImU32 col, ImGuiDir dir, float scale = 1.0f);    /* original C++ signature */
def render_arrow(
    draw_list: ImDrawList, pos: ImVec2, col: ImU32, dir: Dir, scale: float = 1.0
) -> None:
    pass

# IMGUI_API void          RenderBullet(ImDrawList* draw_list, ImVec2 pos, ImU32 col);    /* original C++ signature */
def render_bullet(draw_list: ImDrawList, pos: ImVec2, col: ImU32) -> None:
    pass

# IMGUI_API void          RenderCheckMark(ImDrawList* draw_list, ImVec2 pos, ImU32 col, float sz);    /* original C++ signature */
def render_check_mark(
    draw_list: ImDrawList, pos: ImVec2, col: ImU32, sz: float
) -> None:
    pass

# IMGUI_API void          RenderArrowPointingAt(ImDrawList* draw_list, ImVec2 pos, ImVec2 half_sz, ImGuiDir direction, ImU32 col);    /* original C++ signature */
def render_arrow_pointing_at(
    draw_list: ImDrawList, pos: ImVec2, half_sz: ImVec2, direction: Dir, col: ImU32
) -> None:
    pass

# IMGUI_API void          RenderArrowDockMenu(ImDrawList* draw_list, ImVec2 p_min, float sz, ImU32 col);    /* original C++ signature */
def render_arrow_dock_menu(
    draw_list: ImDrawList, p_min: ImVec2, sz: float, col: ImU32
) -> None:
    pass

# IMGUI_API void          RenderRectFilledRangeH(ImDrawList* draw_list, const ImRect& rect, ImU32 col, float x_start_norm, float x_end_norm, float rounding);    /* original C++ signature */
def render_rect_filled_range_h(
    draw_list: ImDrawList,
    rect: ImRect,
    col: ImU32,
    x_start_norm: float,
    x_end_norm: float,
    rounding: float,
) -> None:
    pass

# IMGUI_API void          RenderRectFilledWithHole(ImDrawList* draw_list, const ImRect& outer, const ImRect& inner, ImU32 col, float rounding);    /* original C++ signature */
def render_rect_filled_with_hole(
    draw_list: ImDrawList, outer: ImRect, inner: ImRect, col: ImU32, rounding: float
) -> None:
    pass

# IMGUI_API ImDrawFlags   CalcRoundingFlagsForRectInRect(const ImRect& r_in, const ImRect& r_outer, float threshold);    /* original C++ signature */
def calc_rounding_flags_for_rect_in_rect(
    r_in: ImRect, r_outer: ImRect, threshold: float
) -> ImDrawFlags:
    pass

# Widgets
# IMGUI_API void          TextEx(const char* text, const char* text_end = NULL, ImGuiTextFlags flags = 0);    /* original C++ signature */
def text_ex(text: str, text_end: Optional[str] = None, flags: TextFlags = 0) -> None:
    pass

# IMGUI_API bool          ButtonEx(const char* label, const ImVec2& size_arg = ImVec2(0, 0), ImGuiButtonFlags flags = 0);    /* original C++ signature */
def button_ex(
    label: str, size_arg: ImVec2 = ImVec2(0, 0), flags: ButtonFlags = 0
) -> bool:
    pass

# IMGUI_API bool          ArrowButtonEx(const char* str_id, ImGuiDir dir, ImVec2 size_arg, ImGuiButtonFlags flags = 0);    /* original C++ signature */
def arrow_button_ex(
    str_id: str, dir: Dir, size_arg: ImVec2, flags: ButtonFlags = 0
) -> bool:
    pass

# IMGUI_API bool          ImageButtonEx(ImGuiID id, ImTextureID texture_id, const ImVec2& image_size, const ImVec2& uv0, const ImVec2& uv1, const ImVec4& bg_col, const ImVec4& tint_col, ImGuiButtonFlags flags = 0);    /* original C++ signature */
def image_button_ex(
    id_: ID,
    texture_id: ImTextureID,
    image_size: ImVec2,
    uv0: ImVec2,
    uv1: ImVec2,
    bg_col: ImVec4,
    tint_col: ImVec4,
    flags: ButtonFlags = 0,
) -> bool:
    pass

# IMGUI_API void          SeparatorEx(ImGuiSeparatorFlags flags, float thickness = 1.0f);    /* original C++ signature */
def separator_ex(flags: SeparatorFlags, thickness: float = 1.0) -> None:
    pass

# IMGUI_API void          SeparatorTextEx(ImGuiID id, const char* label, const char* label_end, float extra_width);    /* original C++ signature */
def separator_text_ex(id_: ID, label: str, label_end: str, extra_width: float) -> None:
    pass

# IMGUI_API bool          CheckboxFlags(const char* label, ImS64* flags, ImS64 flags_value);    /* original C++ signature */
@overload
def checkbox_flags(label: str, flags: ImS64, flags_value: ImS64) -> bool:
    pass

# IMGUI_API bool          CheckboxFlags(const char* label, ImU64* flags, ImU64 flags_value);    /* original C++ signature */
@overload
def checkbox_flags(label: str, flags: ImU64, flags_value: ImU64) -> bool:
    pass

# Widgets: Window Decorations
# IMGUI_API bool          CloseButton(ImGuiID id, const ImVec2& pos);    /* original C++ signature */
def close_button(id_: ID, pos: ImVec2) -> bool:
    pass

# IMGUI_API bool          CollapseButton(ImGuiID id, const ImVec2& pos, ImGuiDockNode* dock_node);    /* original C++ signature */
def collapse_button(id_: ID, pos: ImVec2, dock_node: DockNode) -> bool:
    pass

# IMGUI_API void          Scrollbar(ImGuiAxis axis);    /* original C++ signature */
def scrollbar(axis: Axis) -> None:
    pass

# IMGUI_API bool          ScrollbarEx(const ImRect& bb, ImGuiID id, ImGuiAxis axis, ImS64* p_scroll_v, ImS64 avail_v, ImS64 contents_v, ImDrawFlags flags);    /* original C++ signature */
def scrollbar_ex(
    bb: ImRect,
    id_: ID,
    axis: Axis,
    p_scroll_v: ImS64,
    avail_v: ImS64,
    contents_v: ImS64,
    flags: ImDrawFlags,
) -> bool:
    pass

# IMGUI_API ImRect        GetWindowScrollbarRect(ImGuiWindow* window, ImGuiAxis axis);    /* original C++ signature */
def get_window_scrollbar_rect(window: Window, axis: Axis) -> ImRect:
    pass

# IMGUI_API ImGuiID       GetWindowScrollbarID(ImGuiWindow* window, ImGuiAxis axis);    /* original C++ signature */
def get_window_scrollbar_id(window: Window, axis: Axis) -> ID:
    pass

# IMGUI_API ImGuiID       GetWindowResizeCornerID(ImGuiWindow* window, int n);     /* original C++ signature */
def get_window_resize_corner_id(window: Window, n: int) -> ID:
    """0..3: corners"""
    pass

# IMGUI_API ImGuiID       GetWindowResizeBorderID(ImGuiWindow* window, ImGuiDir dir);    /* original C++ signature */
def get_window_resize_border_id(window: Window, dir: Dir) -> ID:
    pass

# Widgets low-level behaviors
# IMGUI_API bool          ButtonBehavior(const ImRect& bb, ImGuiID id, bool* out_hovered, bool* out_held, ImGuiButtonFlags flags = 0);    /* original C++ signature */
def button_behavior(
    bb: ImRect, id_: ID, out_hovered: bool, out_held: bool, flags: ButtonFlags = 0
) -> Tuple[bool, bool, bool]:
    pass

# IMGUI_API bool          DragBehavior(ImGuiID id, ImGuiDataType data_type, void* p_v, float v_speed, const void* p_min, const void* p_max, const char* format, ImGuiSliderFlags flags);    /* original C++ signature */
def drag_behavior(
    id_: ID,
    data_type: DataType,
    p_v: Any,
    v_speed: float,
    p_min: Any,
    p_max: Any,
    format: str,
    flags: SliderFlags,
) -> bool:
    pass

# IMGUI_API bool          SliderBehavior(const ImRect& bb, ImGuiID id, ImGuiDataType data_type, void* p_v, const void* p_min, const void* p_max, const char* format, ImGuiSliderFlags flags, ImRect* out_grab_bb);    /* original C++ signature */
def slider_behavior(
    bb: ImRect,
    id_: ID,
    data_type: DataType,
    p_v: Any,
    p_min: Any,
    p_max: Any,
    format: str,
    flags: SliderFlags,
    out_grab_bb: ImRect,
) -> bool:
    pass

# IMGUI_API bool          SplitterBehavior(const ImRect& bb, ImGuiID id, ImGuiAxis axis, float* size1, float* size2, float min_size1, float min_size2, float hover_extend = 0.0f, float hover_visibility_delay = 0.0f, ImU32 bg_col = 0);    /* original C++ signature */
def splitter_behavior(
    bb: ImRect,
    id_: ID,
    axis: Axis,
    size1: float,
    size2: float,
    min_size1: float,
    min_size2: float,
    hover_extend: float = 0.0,
    hover_visibility_delay: float = 0.0,
    bg_col: ImU32 = 0,
) -> Tuple[bool, float, float]:
    pass

# IMGUI_API bool          TreeNodeBehavior(ImGuiID id, ImGuiTreeNodeFlags flags, const char* label, const char* label_end = NULL);    /* original C++ signature */
def tree_node_behavior(
    id_: ID, flags: TreeNodeFlags, label: str, label_end: Optional[str] = None
) -> bool:
    pass

# IMGUI_API void          TreePushOverrideID(ImGuiID id);    /* original C++ signature */
def tree_push_override_id(id_: ID) -> None:
    pass

# IMGUI_API void          TreeNodeSetOpen(ImGuiID id, bool open);    /* original C++ signature */
def tree_node_set_open(id_: ID, open: bool) -> None:
    pass

# IMGUI_API bool          TreeNodeUpdateNextOpen(ImGuiID id, ImGuiTreeNodeFlags flags);       /* original C++ signature */
def tree_node_update_next_open(id_: ID, flags: TreeNodeFlags) -> bool:
    """Return open state. Consume previous SetNextItemOpen() data, if any. May return True when logging."""
    pass

# IMGUI_API void          SetNextItemSelectionUserData(ImGuiSelectionUserData selection_user_data);    /* original C++ signature */
def set_next_item_selection_user_data(selection_user_data: SelectionUserData) -> None:
    pass

# Template functions are instantiated in imgui_widgets.cpp for a finite number of types.
# To use them externally (for custom widget) you may need an "extern template" statement in your code in order to link to existing instances and silence Clang warnings (see #2036).
# e.g. " extern template IMGUI_API float RoundScalarWithFormatT<float, float>(const char* format, ImGuiDataType data_type, float v); "

# Data type helpers

# InputText
# IMGUI_API void          InputTextDeactivateHook(ImGuiID id);    /* original C++ signature */
def input_text_deactivate_hook(id_: ID) -> None:
    pass

# inline ImGuiInputTextState* GetInputTextState(ImGuiID id)   { ImGuiContext& g = *GImGui; return (id != 0 && g.InputTextState.ID == id) ? &g.InputTextState : NULL; }     /* original C++ signature */
def get_input_text_state(id_: ID) -> InputTextState:
    """(private API)

    Get input text state if active
    """
    pass

# Color
# IMGUI_API void          ColorTooltip(const char* text, const float* col, ImGuiColorEditFlags flags);    /* original C++ signature */
def color_tooltip(text: str, col: float, flags: ColorEditFlags) -> None:
    pass

# IMGUI_API void          ColorEditOptionsPopup(const float* col, ImGuiColorEditFlags flags);    /* original C++ signature */
def color_edit_options_popup(col: float, flags: ColorEditFlags) -> None:
    pass

# IMGUI_API void          ColorPickerOptionsPopup(const float* ref_col, ImGuiColorEditFlags flags);    /* original C++ signature */
def color_picker_options_popup(ref_col: float, flags: ColorEditFlags) -> None:
    pass

# Shade functions (write over already created vertices)
# IMGUI_API void          ShadeVertsLinearColorGradientKeepAlpha(ImDrawList* draw_list, int vert_start_idx, int vert_end_idx, ImVec2 gradient_p0, ImVec2 gradient_p1, ImU32 col0, ImU32 col1);    /* original C++ signature */
def shade_verts_linear_color_gradient_keep_alpha(
    draw_list: ImDrawList,
    vert_start_idx: int,
    vert_end_idx: int,
    gradient_p0: ImVec2,
    gradient_p1: ImVec2,
    col0: ImU32,
    col1: ImU32,
) -> None:
    pass

# IMGUI_API void          ShadeVertsLinearUV(ImDrawList* draw_list, int vert_start_idx, int vert_end_idx, const ImVec2& a, const ImVec2& b, const ImVec2& uv_a, const ImVec2& uv_b, bool clamp);    /* original C++ signature */
def shade_verts_linear_uv(
    draw_list: ImDrawList,
    vert_start_idx: int,
    vert_end_idx: int,
    a: ImVec2,
    b: ImVec2,
    uv_a: ImVec2,
    uv_b: ImVec2,
    clamp: bool,
) -> None:
    pass

# IMGUI_API void          ShadeVertsTransformPos(ImDrawList* draw_list, int vert_start_idx, int vert_end_idx, const ImVec2& pivot_in, float cos_a, float sin_a, const ImVec2& pivot_out);    /* original C++ signature */
def shade_verts_transform_pos(
    draw_list: ImDrawList,
    vert_start_idx: int,
    vert_end_idx: int,
    pivot_in: ImVec2,
    cos_a: float,
    sin_a: float,
    pivot_out: ImVec2,
) -> None:
    pass

# Garbage collection
# IMGUI_API void          GcCompactTransientMiscBuffers();    /* original C++ signature */
def gc_compact_transient_misc_buffers() -> None:
    pass

# IMGUI_API void          GcCompactTransientWindowBuffers(ImGuiWindow* window);    /* original C++ signature */
def gc_compact_transient_window_buffers(window: Window) -> None:
    pass

# IMGUI_API void          GcAwakeTransientWindowBuffers(ImGuiWindow* window);    /* original C++ signature */
def gc_awake_transient_window_buffers(window: Window) -> None:
    pass

# Debug Log
# IMGUI_API void          DebugLog(const char* fmt, ...) ;    /* original C++ signature */
def debug_log(fmt: str) -> None:
    pass

# IMGUI_API void          DebugAllocHook(ImGuiDebugAllocInfo* info, int frame_count, void* ptr, size_t size);     /* original C++ signature */
def debug_alloc_hook(
    info: DebugAllocInfo, frame_count: int, ptr: Any, size: int
) -> None:
    """size >= 0 : alloc, size = -1 : free"""
    pass

# Debug Tools
# IMGUI_API void          ErrorCheckUsingSetCursorPosToExtendParentBoundaries();    /* original C++ signature */
def error_check_using_set_cursor_pos_to_extend_parent_boundaries() -> None:
    pass

# [ADAPT_IMGUI_BUNDLE]
# #ifdef IMGUI_BUNDLE_PYTHON_API
#
# IMGUI_API void          ErrorCheckEndFrameRecover(ImGuiErrorStringCallback callback);    /* original C++ signature */
@overload
def error_check_end_frame_recover(callback: ErrorStringCallback) -> None:
    pass

# IMGUI_API void          ErrorCheckEndWindowRecover(ImGuiErrorStringCallback callback);    /* original C++ signature */
@overload
def error_check_end_window_recover(callback: ErrorStringCallback) -> None:
    pass

# #endif
#
# [/ADAPT_IMGUI_BUNDLE]

# IMGUI_API void          DebugDrawCursorPos(ImU32 col = IM_COL32(255, 0, 0, 255));    /* original C++ signature */
def debug_draw_cursor_pos(col: ImU32 = IM_COL32(255, 0, 0, 255)) -> None:
    pass

# IMGUI_API void          DebugDrawLineExtents(ImU32 col = IM_COL32(255, 0, 0, 255));    /* original C++ signature */
def debug_draw_line_extents(col: ImU32 = IM_COL32(255, 0, 0, 255)) -> None:
    pass

# IMGUI_API void          DebugDrawItemRect(ImU32 col = IM_COL32(255, 0, 0, 255));    /* original C++ signature */
def debug_draw_item_rect(col: ImU32 = IM_COL32(255, 0, 0, 255)) -> None:
    pass

# IMGUI_API void          DebugLocateItem(ImGuiID target_id);                         /* original C++ signature */
def debug_locate_item(target_id: ID) -> None:
    """Call sparingly: only 1 at the same time!"""
    pass

# IMGUI_API void          DebugLocateItemOnHover(ImGuiID target_id);                  /* original C++ signature */
def debug_locate_item_on_hover(target_id: ID) -> None:
    """Only call on reaction to a mouse Hover: because only 1 at the same time!"""
    pass

# IMGUI_API void          DebugLocateItemResolveWithLastItem();    /* original C++ signature */
def debug_locate_item_resolve_with_last_item() -> None:
    pass

# inline void             DebugStartItemPicker()                                  { ImGuiContext& g = *GImGui; g.DebugItemPickerActive = true; }    /* original C++ signature */
def debug_start_item_picker() -> None:
    """(private API)"""
    pass

# IMGUI_API void          ShowFontAtlas(ImFontAtlas* atlas);    /* original C++ signature */
def show_font_atlas(atlas: ImFontAtlas) -> None:
    pass

# IMGUI_API void          DebugHookIdInfo(ImGuiID id, ImGuiDataType data_type, const void* data_id, const void* data_id_end);    /* original C++ signature */
def debug_hook_id_info(
    id_: ID, data_type: DataType, data_id: Any, data_id_end: Any
) -> None:
    pass

# IMGUI_API void          DebugNodeColumns(ImGuiOldColumns* columns);    /* original C++ signature */
def debug_node_columns(columns: OldColumns) -> None:
    pass

# IMGUI_API void          DebugNodeDockNode(ImGuiDockNode* node, const char* label);    /* original C++ signature */
def debug_node_dock_node(node: DockNode, label: str) -> None:
    pass

# IMGUI_API void          DebugNodeDrawList(ImGuiWindow* window, ImGuiViewportP* viewport, const ImDrawList* draw_list, const char* label);    /* original C++ signature */
def debug_node_draw_list(
    window: Window, viewport: ViewportP, draw_list: ImDrawList, label: str
) -> None:
    pass

# IMGUI_API void          DebugNodeDrawCmdShowMeshAndBoundingBox(ImDrawList* out_draw_list, const ImDrawList* draw_list, const ImDrawCmd* draw_cmd, bool show_mesh, bool show_aabb);    /* original C++ signature */
def debug_node_draw_cmd_show_mesh_and_bounding_box(
    out_draw_list: ImDrawList,
    draw_list: ImDrawList,
    draw_cmd: ImDrawCmd,
    show_mesh: bool,
    show_aabb: bool,
) -> None:
    pass

# IMGUI_API void          DebugNodeFont(ImFont* font);    /* original C++ signature */
def debug_node_font(font: ImFont) -> None:
    pass

# IMGUI_API void          DebugNodeFontGlyph(ImFont* font, const ImFontGlyph* glyph);    /* original C++ signature */
def debug_node_font_glyph(font: ImFont, glyph: ImFontGlyph) -> None:
    pass

# IMGUI_API void          DebugNodeStorage(ImGuiStorage* storage, const char* label);    /* original C++ signature */
def debug_node_storage(storage: Storage, label: str) -> None:
    pass

# IMGUI_API void          DebugNodeTabBar(ImGuiTabBar* tab_bar, const char* label);    /* original C++ signature */
def debug_node_tab_bar(tab_bar: TabBar, label: str) -> None:
    pass

# IMGUI_API void          DebugNodeTable(ImGuiTable* table);    /* original C++ signature */
def debug_node_table(table: Table) -> None:
    pass

# IMGUI_API void          DebugNodeTableSettings(ImGuiTableSettings* settings);    /* original C++ signature */
def debug_node_table_settings(settings: TableSettings) -> None:
    pass

# IMGUI_API void          DebugNodeInputTextState(ImGuiInputTextState* state);    /* original C++ signature */
def debug_node_input_text_state(state: InputTextState) -> None:
    pass

# IMGUI_API void          DebugNodeTypingSelectState(ImGuiTypingSelectState* state);    /* original C++ signature */
def debug_node_typing_select_state(state: TypingSelectState) -> None:
    pass

# IMGUI_API void          DebugNodeWindow(ImGuiWindow* window, const char* label);    /* original C++ signature */
def debug_node_window(window: Window, label: str) -> None:
    pass

# IMGUI_API void          DebugNodeWindowSettings(ImGuiWindowSettings* settings);    /* original C++ signature */
def debug_node_window_settings(settings: WindowSettings) -> None:
    pass

# IMGUI_API void          DebugNodeWindowsList(ImVector<ImGuiWindow*>* windows, const char* label);    /* original C++ signature */
def debug_node_windows_list(windows: ImVector_Window_ptr, label: str) -> None:
    pass

# IMGUI_API void          DebugNodeViewport(ImGuiViewportP* viewport);    /* original C++ signature */
def debug_node_viewport(viewport: ViewportP) -> None:
    pass

# IMGUI_API void          DebugRenderKeyboardPreview(ImDrawList* draw_list);    /* original C++ signature */
def debug_render_keyboard_preview(draw_list: ImDrawList) -> None:
    pass

# IMGUI_API void          DebugRenderViewportThumbnail(ImDrawList* draw_list, ImGuiViewportP* viewport, const ImRect& bb);    /* original C++ signature */
def debug_render_viewport_thumbnail(
    draw_list: ImDrawList, viewport: ViewportP, bb: ImRect
) -> None:
    pass

# Obsolete functions

# -----------------------------------------------------------------------------
# [SECTION] ImFontAtlas internal API
# -----------------------------------------------------------------------------

class ImFontBuilderIO:
    """This structure is likely to evolve as we add support for incremental atlas updates"""

    # ImFontBuilderIO();    /* original C++ signature */
    def __init__(self) -> None:
        """Auto-generated default constructor"""
        pass

# Helper for font builder
# IMGUI_API void      ImFontAtlasUpdateConfigDataPointers(ImFontAtlas* atlas);    /* original C++ signature */
def im_font_atlas_update_config_data_pointers(atlas: ImFontAtlas) -> None:
    pass

# -----------------------------------------------------------------------------
# [SECTION] Test Engine specific hooks (imgui_test_engine)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------

# #endif

# <submodule im_stb>
class im_stb:  # Proxy class that introduces typings for the *submodule* im_stb
    pass  # (This corresponds to a C++ namespace. All method are static!)

# </submodule im_stb>
####################    </generated_from:imgui_internal.h>    ####################


####################    <generated_from:imgui_internal_pywrappers.h>    ####################
# Part of ImGui Bundle - MIT License - Copyright (c) 2022-2023 Pascal Thomet - https://github.com/pthom/imgui_bundle
# Handwritten wrappers around parts of the imgui API, when needed for the python bindings

# IMGUI_API std::tuple<ImGuiID, ImGuiID, ImGuiID>       DockBuilderSplitNode_Py(ImGuiID node_id, ImGuiDir split_dir, float size_ratio_for_node_at_dir);    /* original C++ signature */
# }
def dock_builder_split_node_py(
    node_id: ID, split_dir: Dir, size_ratio_for_node_at_dir: float
) -> Tuple[ID, ID, ID]:
    """DockBuilderSplitNode_Py() create 2 child nodes within 1 node. The initial node becomes a parent node.
    This version is an adaptation for the python bindings (the C++ version uses two output parameters for the ID of the child nodes, this version returns a tuple)
    """
    pass
####################    </generated_from:imgui_internal_pywrappers.h>    ####################

# </litgen_stub>

# fmt: on
