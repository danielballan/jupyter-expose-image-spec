from setuptools import setup

setup(name='jupyter-expose-image-spec',
      packages=['jupyter_expose_image_spec'],
      include_package_data=True,
      data_files=[
          # like `jupyter serverextension enable --sys-prefix`
          ("etc/jupyter/jupyter_notebook_config.d", [
              "jupyter-config/jupyter_notebook_config.d/jupyter_expose_image_spec.json"
          ])
      ],
      zip_safe=False
)
