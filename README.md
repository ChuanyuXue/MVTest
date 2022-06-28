# MVTest
A Distribution-Free Test of Independence Based on Mean Variance Index.

## Install

    pip install mvtpy
    
## Usage

    from mvtpy.mvtest import mvtest
    model = mvtest()
    y = np.array(range(5))
    x = y + np.random.normal()
    # Y has to be a discrete vector
    model.test(x, y)
    
## Notes

This package is purely achieved with Numpy library with limited execution performance. Please read the reference and speed up the the code by yourself for large scale dataset.

## Reference

Cui H, Zhong W. A Distribution-Free Test of Independence and Its Application to Variable Selection[J]. arXiv preprint arXiv:1801.10559, 2018.

