# k8s-bespin-playground
Various tools used in exploring kubernetes for use in bespin

#  bespinjob
Consists of a jupyter notebook and a supporting library to
- download data from DukeDS 
- running a cwl workflow producing some output
- upload results to DukeDS

https://github.com/johnbradley/k8s-bespin-playground/blob/master/bespinjob/BespinJob.ipynb

# staging
Consists of a couple scripts to stage data in and out of DukeDS and a Dockerfile.
This has been built and temporarily pushed to `jbradley/duke-ds-staging`.
https://github.com/johnbradley/k8s-bespin-playground/blob/master/staging/Dockerfile
