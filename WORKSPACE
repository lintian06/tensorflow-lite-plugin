workspace(name = "org_tensorflow_lite_tensorboard_plugin")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_skylib",
    sha256 = "2c62d8cd4ab1e65c08647eb4afe38f51591f43f7f0885e7769832fa137633dcb",
    strip_prefix = "bazel-skylib-0.7.0",
    urls = [
        # tag 0.7.0 resolves to commit 6741f733227dc68137512161a5ce6fcf283e3f58 (2019-02-08 18:37:26 +0100)
        "http://mirror.tensorflow.org/github.com/bazelbuild/bazel-skylib/archive/0.7.0.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/archive/0.7.0.tar.gz",
    ],
)

load("@bazel_skylib//lib:versions.bzl", "versions")
# Keep this version in sync with the BAZEL environment variable defined
# in our .travis.yml config.
versions.check(minimum_bazel_version = "0.22.0")

http_archive(
    name = "io_bazel_rules_webtesting",
    sha256 = "f89ca8e91ac53b3c61da356c685bf03e927f23b97b086cc593db8edc088c143f",
    urls = [
        # tag 0.3.1 resolves to commit afa8c4435ed8fd832046dab807ef998a26779ecb (2019-04-03 14:10:32 -0700)
        "http://mirror.tensorflow.org/github.com/bazelbuild/rules_webtesting/releases/download/0.3.1/rules_webtesting.tar.gz",
        "https://github.com/bazelbuild/rules_webtesting/releases/download/0.3.1/rules_webtesting.tar.gz",
    ],
)

load("@io_bazel_rules_webtesting//web:repositories.bzl", "web_test_repositories")
web_test_repositories()

load("@io_bazel_rules_webtesting//web:py_repositories.bzl", "py_repositories")
py_repositories()

http_archive(
    name = "io_bazel_rules_closure",
    sha256 = "b6936ecc0b5a1ef616b9d7e76694d414aa5605265c11322257a610fb256b1bf7",
    # The changes that we need for Bazel 0.26 compatibility are not in
    # any release, so we pin to HEAD as of 2019-06-04.
    strip_prefix = "rules_closure-7434c41542ca9e1b05166d897b90073d1b8b2cf8",
    urls = [
        "http://mirror.tensorflow.org/github.com/bazelbuild/rules_closure/archive/7434c41542ca9e1b05166d897b90073d1b8b2cf8.tar.gz",
        "https://github.com/bazelbuild/rules_closure/archive/7434c41542ca9e1b05166d897b90073d1b8b2cf8.tar.gz",  # 2019-06-04
    ],
)

load("@io_bazel_rules_closure//closure:defs.bzl", "closure_repositories")
closure_repositories(
    omit_com_google_protobuf = True,
    omit_com_google_protobuf_js = True,
)

http_archive(
    name = "org_tensorflow",
    sha256 = "1086f63c2c9fbea6873e137d08b5711a0493a5b699f258774da97f7672ba939a",
    strip_prefix = "tensorflow-2243bd6ba9b36d43dbd5c0ede313853f187f5dce",
    urls = [
        "http://mirror.tensorflow.org/github.com/tensorflow/tensorflow/archive/2243bd6ba9b36d43dbd5c0ede313853f187f5dce.tar.gz",  # 2019-03-26
        "https://github.com/tensorflow/tensorflow/archive/2243bd6ba9b36d43dbd5c0ede313853f187f5dce.tar.gz",
    ],
)

load("@org_tensorflow//tensorflow:workspace.bzl", "tf_workspace")
tf_workspace()

#http_archive(
#    name = "org_tensorflow_tensorboard",
#    sha256 = "5d04f587e4597b555f144dc128ddd5a0d8d1b26065d24dddc2b36ac82d9a85dd",
#    strip_prefix = "tensorboard-8de790143b2cb787a8b0f1168cb0dd8d64eb8dcf",
#    urls = [
#        "https://mirror.bazel.build/github.com/tensorflow/tensorboard/archive/8de790143b2cb787a8b0f1168cb0dd8d64eb8dcf.tar.gz",
#        "https://github.com/tensorflow/tensorboard/archive/8de790143b2cb787a8b0f1168cb0dd8d64eb8dcf.tar.gz",  # 2019-01-13
#    ],
#)

#http_archive(
#    name = "org_tensorflow_tensorboard",
#    sha256 = "1e79a1cfe64cb569f71319d4ecf3594d4d7db815ecbfc772a3534c5a13ff4af2",
#    strip_prefix = "tensorboard-78db135e980fff6852cd91f3da439b45e7f9fc1e",
#    urls = [
#        "https://github.com/tensorflow/tensorboard/archive/78db135e980fff6852cd91f3da439b45e7f9fc1e.tar.gz",  # 2019-05-14
#    ],
#)

#http_archive(
#    name = "org_tensorflow_tensorboard",
    # sha256 = "1e79a1cfe64cb569f71319d4ecf3594d4d7db815ecbfc772a3534c5a13ff4af2",
#    strip_prefix = "tensorboard-af7b9874d55257a7b7261aea1501396c6ca6259a",
#    urls = [
#        "https://github.com/lintian06/tensorboard/archive/af7b9874d55257a7b7261aea1501396c6ca6259a.tar.gz",  # 2019-06-17
#    ],
#)

http_archive(
    name = "org_tensorflow_tensorboard_old",
    strip_prefix = "tensorboard-lite_plugin_fix_dep2",
    urls = [
        "https://github.com/lintian06/tensorboard/archive/lite_plugin_fix_dep2.zip",  # Dev version.
    ],
)

git_repository(
    name = "org_tensorflow_tensorboard",
    remote = "https://github.com/lintian06/tensorboard",
)


load("@org_tensorflow_tensorboard//third_party:workspace.bzl", "tensorboard_workspace")
tensorboard_workspace()

# TF Lite Plugin Specific Dependencies
