# CHANGELOG

1. [Tasks](#Tasks)
    1. [Future](#Future)
    2. [In progress](#In-progress)
    3. [Done (Release candidates)](#Done-Release-candidates)
2. [Release Notes](#Release-Notes)
    1. [0.0.0 (2019.07.20)](#000-20190720)

## Tasks

<!-- Tags
NEW : added new feature
FIX : bug fixed
IMPROVE : feature improved
REMOVE : feature removed
OTHER
-->

### Future

- **NEW**: Handle the indirect address section

<!--  -->

- **IMPROVE**: Separate motor and port information from preset
    - (eng) The current form needs to know which port the motor is connected. This is very cumbersome.
    - (kor) 현재의 양식은 모터가 어느 포트에 소속되어 있는지 알아야 합니다. 이것은 매우 번거롭기 때문에 `preset`에서 분리하여 합니다.
- **IMPROVE**: Wrapping more features from the Dynamixel SDK
- **IMPROVE**: Property decorator
- **IMPROVE**: `DxlMotor`. Customizable path for control table
- **IMPROVE**: Singleton with arguments. Duplicate `dxl_helper` issue

<!--  -->

- **OTHER**: [[PEP 257](https://www.python.org/dev/peps/pep-0257/)] Comment for all functions

### In progress

- **NEW** Control tables of all dxl motors

### Done (Release candidates)

---

## Release Notes

<!-- Tags
NEW : added new feature
FIXED : bug fixed
IMPROVED : feature improved
REMOVED : feature removed
OTHER
-->

### 0.0.0 (2019.07.20)

1st Release! Yeah!

- **NEW**: 2 Basic features (torque on/off and position command)
- **NEW**: Apply [CodeFactor](https://www.codefactor.io/) to manage code quality
- **NEW**: Basic tutorials

<!--  -->

- **OTHER**: Test basic features with actual motor(XM430-W210) in Python 2.x and 3.x

---

<!--  -->

<!-- EXAMPLE

- **New** Prefer unused links for reference link label completions ([#414](https://github.com/yzhang-gh/vscode-markdown/issues/414)). Thanks, [Chris (@alshain)](https://github.com/alshain).
- **New**: Option `markdown.extension.print.onFileSave` ([#417](https://github.com/yzhang-gh/vscode-markdown/issues/417)). Thanks, [Li Yiming (@upupming)](https://github.com/upupming).
- **New**: Autocompletion for heading links ([#419](https://github.com/yzhang-gh/vscode-markdown/issues/419)). Thanks again, [Chris (@alshain)](https://github.com/alshain).

-->
<!--  -->
<!--

- **Fix**: Syntax decorations ([#390](https://github.com/yzhang-gh/vscode-markdown/issues/390)).
- **Fix**: Table formatter ([#408](https://github.com/yzhang-gh/vscode-markdown/issues/408)).
- **Fix**: Delete space rather than outdent list when there are two or more spaces on <kbd>Backspace</kbd> ([#410](https://github.com/yzhang-gh/vscode-markdown/issues/410)).
- **Fix**: Image paths in exported HTML ([#415](https://github.com/yzhang-gh/vscode-markdown/issues/415), [#429](https://github.com/yzhang-gh/vscode-markdown/issues/429)).
- **Fix**: TOC and fenced code blocks ([#425](https://github.com/yzhang-gh/vscode-markdown/issues/425)).
- **Other**: Sort KaTeX functions (lowercase first) ([#413](https://github.com/yzhang-gh/vscode-markdown/issues/413)).
- **Other**: Update KaTeX supported functions ([#416](https://github.com/yzhang-gh/vscode-markdown/issues/416)). Thanks again, [Li Yiming (@upupming)](https://github.com/upupming).

-->
