import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = [
    'werkzeug >= 0.11.15',
    'tensorboard >= 1.13.0',
]

setuptools.setup(
    name="tensorboard_lite_plugin",
    version="0.0.1",
    author="TensorFlow Lite team",
    author_email="author@example.com",
    description="TF Lite Plugin for TensorBoard.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github./pypa/sampleproject",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "tensorboard_plugins": [
            "lite_plugin=tensorboard_lite_plugin.lite_plugin:LitePlugin",
        ],
    },
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)