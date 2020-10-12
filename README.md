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
    
## Notice
This package only performs acceptable efficiency on large-scale dataset due to my limited programming skills. If you have any better solution on this algorithm, please contact me at cs_xcy@126.com

## Reference

Cui H, Zhong W. A Distribution-Free Test of Independence and Its Application to Variable Selection[J]. arXiv preprint arXiv:1801.10559, 2018.

