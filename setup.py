from distutils.core import setup
setup(
    name='nipype-batch-workflows',
    version='1.0.1',
    author='https://www.ctsi.ufl.edu/research/study-development/informatics-consulting/',
    author_email='ctsit@ctsi.ufl.edu',
    description='Neuroimaging workflows writtten in nipype with a focus on using a job scheduler',
    long_description=open('README.md').read(),
    url='https://github.com/ctsit/nipype-pbs-workflows',
    packages=['nipype-batch-workflows'],
    package_dir={'nipype-batch-workflows': 'src'},
    scripts=['src/bedpostx.py', 'src/dcm2niiconverter.py'],
)
