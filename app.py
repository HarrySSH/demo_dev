# ------------------------------------------------------------------------------
# Copyright (c) 2023, Alaa lab, UC Berkeley. All rights reserved.
#
# Written by Harry(Shenghuan) Sun
# ------------------------------------------------------------------------------

from __future__ import annotations

import math
import cv2
import random
from fnmatch import fnmatch
import numpy as np

import gradio as gr
import torch
from PIL import Image, ImageOps

title = "Dr-LLaVA: Visual Instruction Tuning with Symbolic Clinical Grounding"

description = """
<p style='text-align: center'> Shenghuan Sun, Gregory Goldgof, Alex Schubert, Zhiqing Sun, Atul Butte, Ahmed Alaa <br>
This is the demo for Dr-LLaVA. So far it could only be used for H&E stained Bone Marrow Aspirate images application.</p>

<b>Tips for using this demo:</b>
<ul>
    <li>Drop a single image from a bone marrow aspirate whole slide image taken at 40x.</li>
</ul>

<p style='text-align: center'>Note: This demo is for research and exploration only.</p>

<div style="text-align: center;">
  <img src="https://i.postimg.cc/tJzyq5Dh/Dr-LLa-VA-Fig-1.png" alt="Application of DrLLaVA to new test images & This demo is for research, exploration only." width="600">
</div>
"""

with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center; margin-bottom: 1rem'>" + title + "</h1>")
    gr.Markdown(description)
    
    with gr.Row():
        with gr.Column():
            # Replace 'path_to_image' with the path to your image file
            gr.Image(value="https://i.postimg.cc/tJzyq5Dh/Dr-LLa-VA-Fig-1.png", 
                     width=600, interactive=False, type="pil")

        with gr.Column():
            generate_button = gr.Button("Generate result")
            load_example_button = gr.Button("Load example")

demo.launch(inline=True, debug=True)

