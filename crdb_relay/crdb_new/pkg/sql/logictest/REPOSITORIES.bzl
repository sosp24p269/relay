# DO NOT EDIT THIS FILE MANUALLY! Use `release update-releases-file`.
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

_PREDECESSOR_VERSION = "23.1.12"
CONFIG_LINUX_AMD64 = "linux-amd64"
CONFIG_LINUX_ARM64 = "linux-arm64"
CONFIG_DARWIN_AMD64 = "darwin-10.9-amd64"
CONFIG_DARWIN_ARM64 = "darwin-11.0-arm64"
_CONFIGS = [
    (CONFIG_LINUX_AMD64, "980ff363521922725c63814696a7385943ca46f3c0bea21322ded9591de33ed2"),
    (CONFIG_LINUX_ARM64, "b55590d6563bb95def500c551b4adb463a5e6b50eb01f4eda8a1c45e41564e78"),
    (CONFIG_DARWIN_AMD64, "0d84b44e62781de3e4520fb015e8a1f1a693007f2e81fca6bc2abf86e7f4d3cc"),
    (CONFIG_DARWIN_ARM64, "892b75bb4b5173634205b731815f42e4c6f36d10fd4a652081631c32fd511e5e"),
]

def _munge_name(s):
    return s.replace("-", "_").replace(".", "_")

def _repo_name(config_name):
    return "cockroach_binary_v{}_{}".format(
        _munge_name(_PREDECESSOR_VERSION),
        _munge_name(config_name))

def _file_name(config_name):
    return "cockroach-v{}.{}/cockroach".format(
        _PREDECESSOR_VERSION, config_name)

def target(config_name):
    return "@{}//:{}".format(_repo_name(config_name),
                             _file_name(config_name))

def cockroach_binaries_for_testing():
    for config in _CONFIGS:
        config_name, shasum = config
        file_name = _file_name(config_name)
        http_archive(
            name = _repo_name(config_name),
            build_file_content = """exports_files(["{}"])""".format(file_name),
            sha256 = shasum,
            urls = [
                "https://binaries.cockroachdb.com/{}".format(
                    file_name.removesuffix("/cockroach")) + ".tgz",
            ],
        )
