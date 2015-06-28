from networkx.addons.metis import types
__all__ = ['MetisError']


class MetisError(Exception):
    """Error returned by METIS"""

    def __init__(self, rstatus, msg):
        """Initializes a MetisError object.

        Parameters
        ----------
        rstatus : int
            Error code returned by METIS.

        msg : string
            Error message returned by METIS.
        """
        super(MetisError, self).__init__('{0}: {1}'.format(
            types.MetisRStatus(rstatus).name, msg))
