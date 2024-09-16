from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(name="some_module.__init__", sources=["some_module/__init__.pyx"]),
        Extension(name="some_module.sub_mod", sources=["some_module/sub_mod.pyx"]),
    ]
)
