# MVTest
A Distribution-Free Test of Independence Based on Mean Variance Index.

## Installation

    pip install mvtpy
    
## Usage

    from mvtpy.mvtest import mvtest
    sample = mvtest()
    y = np.array(range(5))
    x = y + np.random.normal()
    # Y has to be a discrete vector
    sample.test(x, y)
    
## Notes

This package is purely achieved with Numpy library in limited execution performance. Please read the reference and speed up the process by yourself to evaluate large dataset.

## Reference

Cui H, Zhong W. A Distribution-Free Test of Independence and Its Application to Variable Selection[J]. arXiv preprint arXiv:1801.10559, 2018.

