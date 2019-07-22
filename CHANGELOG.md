# CHANGELOG

1. [Tasks](#tasks)
    1. [Future](#future)
    2. [Done (Release Candidates)](#done-release-candidates)
2. [Release Notes](#release-notes)
    1. [0.0.0 (2019.07.22)](#000-20190722)

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
- **NEW**: Supports multiple robot connections with the same ID configuration
- **NEW**: Control tables of all dxl motors
- **NEW**: Basic tutorials

<!--  -->

- **IMPROVE**: Separate motor and port information from `preset`
    - (eng) The current form needs to know which motors connected in which port. This is very cumbersome.
    - (kor) 현재의 양식은 모터가 어느 포트에 소속되어 있는지 알아야 합니다. 이것은 매우 번거롭기 때문에 `preset`에서 분리하려 합니다.
- **IMPROVE**: Wrapping more features from the Dynamixel SDK
- **IMPROVE**: Property decorator
- **IMPROVE**: `DxlMotor`. Customizable path for control table
- **IMPROVE**: Singleton with arguments. Duplicate `dxl_helper` issue

<!--  -->

- **OTHER**: ([PEP 257](https://www.python.org/dev/peps/pep-0257/)) Comment for all functions

### Done (Release Candidates)

---

## Release Notes

<!-- Tags
NEW : added new feature
FIXED : bug fixed
IMPROVED : feature improved
REMOVED : feature removed
OTHER
TESTED
-->

### 0.0.0 (2019.07.22)

1st Release! Yeah!

- **NEW**: 2 Basic features (torque on/off and position command)
- **NEW**: Apply [CodeFactor](https://www.codefactor.io/) to manage code quality
- **NEW**: Multilangual README and tutorials (We are using [Multilingual Markdown Generator](https://github.com/ryul1206/multilingual-markdown)!!)

<!--  -->

- **TESTED**: Test basic features with actual motor(XM430-W210) in Python 2.x and 3.x

---

<!-- EXAMPLE

- **New** Prefer unused links for reference link label completions ([#414](https://github.com/yzhang-gh/vscode-markdown/issues/414)). Thanks, [Chris (@alshain)](https://github.com/alshain).
- **Fix**: TOC and fenced code blocks ([#425](https://github.com/yzhang-gh/vscode-markdown/issues/425)).
- **Other**: Sort KaTeX functions (lowercase first) ([#413](https://github.com/yzhang-gh/vscode-markdown/issues/413)).
- **Other**: Update KaTeX supported functions ([#416](https://github.com/yzhang-gh/vscode-markdown/issues/416)). Thanks again, [Li Yiming (@upupming)](https://github.com/upupming).

-->
