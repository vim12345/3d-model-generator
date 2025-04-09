import torch
import os
import sys
from shap_e.diffusion.sample import sample_latents
from shap_e.diffusion.gaussian_diffusion import create_gaussian_diffusion
from shap_e.models.text_to_3d import create_model_and_diffusion
from shap_e.util.notebooks import decode_latent_mesh

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Create model and diffusion
xm, diffusion = create_model_and_diffusion(xm_dim=256, device=device)
xm.eval()

prompt = sys.argv[1] if len(sys.argv) > 1 else input("Enter a prompt to generate 3D model: ")

# Generate sample
latents = sample_latents(
    batch_size=1,
    model=xm,
    diffusion=diffusion,
    guidance_scale=15.0,
    model_kwargs=dict(texts=[prompt]),
    progress=True,
    clip_denoised=True,
    device=device,
)

# Decode and save
os.makedirs("outputs", exist_ok=True)
for i, latent in enumerate(latents):
    mesh = decode_latent_mesh(xm, latent).tri_mesh()
    out_path = f"outputs/{prompt.replace(' ', '_')}_{i}.glb"
    mesh.write_glb(out_path)
    print(f"Saved: {out_path}")
