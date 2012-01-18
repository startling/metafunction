from distutils.core import setup
import metafunction


setup(
    name = "metafunction",
    version = metafunction.__version__,
    author = "startling",
    author_email = "tdixon51793@gmail.com",
    description = "Haskell-inspired higher-order functions in Python.",
    packages = ["metafunction"],
)
