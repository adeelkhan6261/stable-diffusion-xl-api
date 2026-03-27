from setuptools import setup, find_packages
from pathlib import Path

base_path = Path(__file__).parent
long_description = (base_path / "README.md").read_text(encoding="utf-8")

setup(
    name='sdxl',
    version='1.0.0',
    author='Adeel Ghauri',
    license='MIT',
    author_email='',
    description='Python API wrapper for Stable Diffusion XL — generate stunning 1024×1024 AI images with a single function call.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/adeelkhan6261/stable-diffusion-xl-api/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'stable diffusion', 'sdxl', 'ai', 'image generation',
        'text-to-image', 'replicate', 'api', 'wrapper'
    ],
    install_requires=[
        'requests',
        'flask',
    ],
    python_requires='>=3.8',
)
