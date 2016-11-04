## nipype-workflows

This repository consists of neuroimaging workflows written in nipype with a focus on using a batch system via a job scheduler.
It provides tools and documentation to neuroscientists for using HiPerGator supercomputer at UFRC (UF Research Computing).

### Installation

In order to run the code provided in this repository the following software need to be available:

 - Job scheduler
 - Required Modules:
  - python (version 2.7.6)
  - nipype (version 0.8)
  - fsl (version 5.0.5)
  - mricron (version 6/2013)

Before running the code, the required modules need to be loaded as follows:

```
module load python/2.7.6 nipype/0.8 fsl/5.0.5 mricron/201306
```

### Contributors

 - Philip Chase
 - Mohan Katragadda
 - Ruchi Desai
 - Oleksandr Moskalenko

### License

New BSD License which can be found in the [LICENSE file](https://github.com/ctsit/nipype-pbs-workflows/blob/master/LICENSE)
