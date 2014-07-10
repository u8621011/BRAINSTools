# -*- coding: utf8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class dtiaverageInputSpec(CommandLineInputSpec):
    inputs = InputMultiPath(File(exists=True), desc="List of all the tensor fields to be averaged", argstr="--inputs %s...")
    tensor_output = traits.Either(traits.Bool, File(), hash_files=False, desc="Averaged tensor volume", argstr="--tensor_output %s")
    DTI_double = traits.Bool(desc="Tensor components are saved as doubles (cannot be visualized in Slicer)", argstr="--DTI_double ")
    verbose = traits.Bool(desc="produce verbose output", argstr="--verbose ")


class dtiaverageOutputSpec(TraitedSpec):
    tensor_output = File(desc="Averaged tensor volume", exists=True)


class dtiaverage(SEMLikeCommandLine):

    """title: DTIAverage

category: Diffusion.NIRALPipeline.OnlyCommandLine

description:  
dtiaverage is a program that allows to compute the average of an arbitrary number of tensor fields (listed after the --inputs option) This program is used in our pipeline as the last step of the atlas building processing. When all the tensor fields have been deformed in the same space, to create the average tensor field (--tensor_output) we use dtiaverage. 
 Several average method can be used (specified by the --method option): euclidian, log-euclidian and pga. The default being euclidian.

version: 1.0.0

documentation-url: http://www.google.com/

license: 
    Copyright (c)  Casey Goodlett. All rights reserved.
    See http://www.ia.unc.edu/dev/Copyright.htm for details.
    This software is distributed WITHOUT ANY WARRANTY; without even
    the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
    PURPOSE.  See the above copyright notices for more information.


contributor: Casey Goodlett

"""

    input_spec = dtiaverageInputSpec
    output_spec = dtiaverageOutputSpec
    _cmd = " dtiaverage "
    _outputs_filenames = {'tensor_output': 'tensor_output.nii'}


class fiberstatsInputSpec(CommandLineInputSpec):
    fiber_file = File(desc="DTI Fiber File", exists=True, argstr="--fiber_file %s")
    verbose = traits.Bool(desc="produce verbose output", argstr="--verbose ")


class fiberstatsOutputSpec(TraitedSpec):
    pass


class fiberstats(SEMLikeCommandLine):

    """title: FiberStats

category: Diffusion.NIRALPipeline.OnlyCommandLine

description:  Obsolete tool - Not used anymore

version: 1.1.0

documentation-url: http://www.google.com/

license: 
  Copyright (c)  Casey Goodlett. All rights reserved.
  See http://www.ia.unc.edu/dev/Copyright.htm for details.
     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notices for more information.


contributor: Casey Goodlett

acknowledgements: Hans Johnson(1,3,4); Kent Williams(1); (1=University of Iowa Department of Psychiatry, 3=University of Iowa Department of Biomedical Engineering, 4=University of Iowa Department of Electrical and Computer Engineering) provided conversions to make DTIProcess compatible with Slicer execution, and simplified the stand-alone build requirements by removing the dependancies on boost and a fortran compiler.

"""

    input_spec = fiberstatsInputSpec
    output_spec = fiberstatsOutputSpec
    _cmd = " fiberstats "
    _outputs_filenames = {}
