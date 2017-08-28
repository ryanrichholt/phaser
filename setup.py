from distutils.core import setup, Extension


setup(
  name = 'phaser',
  description = 'phASER Read Variant Mapper',
  packages = ['phaser', 'phaser_annotate', 'phaser_gene_ae'],
  setup_requires=[
        # Setuptools 18.0 properly handles Cython extensions.
        'setuptools>=18.0',
	'Cython',
	'scipy',
	'pysam',
    ],

  entry_points = {
    'console_scripts': [
        'phaser = phaser.phaser:main',
        'phaser-annotate = phaser_annotate.phaser_annotate:main',
        'phaser-gene-ae = phaser_gene_ae.phaser_gene_ae:main',
    ]
  },

  ext_modules=[
        Extension(
            'mylib',
            sources=['phaser/read_variant_map.pyx'],
        ),
    ],
)
