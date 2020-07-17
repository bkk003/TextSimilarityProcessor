import setuptools


def get_description(file_name):
    """ replace the license content while creating the package"""
    with open(file_name, "r", encoding="utf8") as fh:
        description = fh.read()
        return description

with open("README.md", "r") as fh:
    long_description = fh.read()
    if "[MAINTAINERS.md](MAINTAINERS.md)" in long_description:
        long_description = long_description.replace("[MAINTAINERS.md](MAINTAINERS.md)",
                                                    str(get_description("MAINTAINERS.md")))

    if "[INSTALL.md](INSTALL.md)" in long_description:
        long_description = long_description.replace("[INSTALL.md](INSTALL.md)", str(get_description("INSTALL.md")))
        
    if "[License.md](LICENSE.md)" in long_description:
        long_description = long_description.replace("[License.md](LICENSE.md)", str(get_description("LICENSE.md")))

with open('requirements.txt') as f:
    required = f.read().splitlines()
    
setuptools.setup(
    name="similarity_processor",
    version_config={
        "version_format": "{tag}.dev{sha}",
        "starting_version": "0.0.1"
    },
    #version="0.0.3",
    setup_requires=['better-setuptools-git-version'],
    author="Brijesh",
    author_email="brijesh.krishnank@philips.com",
    description="Text Similarity Processor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/philips-software/TextSimilarityProcessor",
    # packages=setuptools.find_packages(exclude=['test', '*.test', '*.test.*']),
    packages=setuptools.find_packages(include=['similarity_processor', 'spell_check'],
                                      exclude=['test', '*.test', '*.test.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    python_requires='>=3.7',
)
