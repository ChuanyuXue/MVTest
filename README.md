# MVTest
A Distribution-Free Test of Independence Based on Mean Variance Index.

## Installation

    pip install MVTPY
    
## Usage

    from MVTPY.mvtest import mvtest
    sample = mvtest()
    y = np.linspace(0,5,5)
    x = y + np.random.normal()
    # Y has to be a discrete vector
    sample.test(x, y)
    
## Reference

Cui H, Zhong W. A Distribution-Free Test of Independence and Its Application to Variable Selection[J]. arXiv preprint arXiv:1801.10559, 2018.

