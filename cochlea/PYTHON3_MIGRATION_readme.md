# Python 3 Migration Notes


THIS DOCUMENT WAS WRITTEN BY COPILOT.

This branch (`py3-zilany2014`) contains Python 3 compatibility updates for the cochlea package.

## Overview

This fork updates the cochlea package to work with Python 3.x, focusing on the `zilany2014` auditory nerve model. The original package was designed for Python 2.x.

## Installation

### From GitHub (Recommended)

```bash
pip install git+https://github.com/YOUR_USERNAME/cochlea.git@py3-zilany2014
```

### From Local Repository

```bash
git clone https://github.com/YOUR_USERNAME/cochlea.git
cd cochlea
git checkout py3-zilany2014
pip install -e .
```

## Migration Status

| Module | Status | Notes |
|--------|--------|-------|
| `zilany2014` | ✅ Migrated | Fully functional with Python 3 |
| `zilany2014_rate` | ✅ Migrated | Fully functional with Python 3 |
| `zilany2009` | Temporarily disabled (see __init__.py) |
| `holmberg2007` | Temporarily disabled (see __init__.py) |
| `holmberg2007_vesicles` | Temporarily disabled (see __init__.py) |

## Changes Made

### Core Changes

1. **Cython Module Updates (`_zilany2014.pyx`)**
   - Updated Cython syntax for Python 3 compatibility
   - Fixed C type declarations and buffer protocols
   - Updated memory view syntax

2. **C Extension Updates**
   - Modified C code for Python 3 C API compatibility
   - Updated `_zilany2014.c` and header files
   - Fixed integer division and print statements

3. **Module Imports (`__init__.py`)**
   - Temporarily commented out Python 2-only modules
   - Added comments indicating migration status
   - Kept `zilany2014` imports active

4. **Print Statements**
   - Converted all `print` statements to `print()` functions
   - Already uses `from __future__ import print_function`

5. **Division Operations**
   - Ensured proper handling of integer vs float division
   - Already uses `from __future__ import division`

### Dependencies

Ensure you have the following installed:
- Python >= 3.6
- NumPy
- Cython
- SciPy (if needed)
- A C compiler (gcc/clang on Linux, MSVC on Windows)

## Usage

### Basic Example

```python
import cochlea
import numpy as np

# Generate a test signal
fs = 100e3  # sampling rate (Hz)
duration = 0.1  # seconds
t = np.arange(0, duration, 1/fs)
sound = np.sin(2 * np.pi * 1000 * t)  # 1 kHz tone

# Set sound level
sound = cochlea.set_dbspl(sound, 60)  # 60 dB SPL

# Run the Zilany 2014 model
anf_trains = cochlea.run_zilany2014(
    sound=sound,
    fs=fs,
    anf_num=(10, 10, 10),  # (HSR, MSR, LSR) fiber counts
    cf=(125, 20000, 100),  # (min_cf, max_cf, num_cf)
    species='cat',
    seed=0
)

print(f"Generated {len(anf_trains)} auditory nerve fibers")
```

### Rate-Level Functions

```python
# Calculate rate-level response
rates = cochlea.run_zilany2014_rate(
    sound=sound,
    fs=fs,
    cf=1000,  # characteristic frequency
    species='cat'
)
```

## Known Issues

- **Modules Not Yet Migrated**: `zilany2009` and `holmberg2007` models are currently disabled
- **Platform Testing**: Primarily tested on Linux; Windows/macOS testing needed
- **Performance**: Performance comparisons with Python 2 version not yet completed

## Testing

To verify the installation works correctly:

```python
import cochlea
import numpy as np

# Quick test
fs = 100e3
sound = np.random.randn(int(0.05 * fs))
sound = cochlea.set_dbspl(sound, 60)

result = cochlea.run_zilany2014(
    sound=sound,
    fs=fs,
    anf_num=(1, 0, 0),
    cf=(1000, 1000, 1),
    species='cat'
)

print("✓ Installation successful!" if len(result) > 0 else "✗ Installation failed")
```

## Contributing

If you encounter issues or want to help migrate the remaining modules:

1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Original Package

This is a fork of the original cochlea package:
- **Original Repository**: [https://github.com/mrkrd/cochlea](https://github.com/mrkrd/cochlea)
- **Original Author**: Marek Rudnicki
- **License**: GNU General Public License v3.0

## Changelog

### Version 3 (Python 3 Migration)
- [Date] Initial Python 3 migration of zilany2014 module
- [Date] Updated Cython bindings for Python 3
- [Date] Fixed C extensions for Python 3 C API

## Contact
For questions about the original package functionality:
- See original repository: https://github.com/mrkrd/cochlea

## License

This fork maintains the same license as the original package:

GNU General Public License v3.0 - see LICENSE file for details.

---

**Last Updated**: January 2026