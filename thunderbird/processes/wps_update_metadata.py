# Processor imports
from pywps import (
    Process,
    ComplexInput,
    FORMATS,
)

# Tool imports
from nchelpers import CFDataset
from dp.update_metadata import main

# Library imports
import logging
from argparse import Namespace


LOGGER = logging.getLogger("PYWPS")


class UpdateMetadata(Process):
    def __init__(self):
        inputs = [
            ComplexInput(
                "netcdf",
                "NetCDF",
                abstract="NetCDF file to update",
                min_occurs=1,
                max_occurs=1,
                supported_formats=[FORMATS.NETCDF],
            ),
            ComplexInput(
                "updates",
                "Updates",
                abstract="JSON file containing updates",
                min_occurs=1,
                max_occurs=1,
                supported_formats=[FORMATS.JSON],
            )
        ]
        outputs = []

        super(UpdateMetadata, self).__init__(
            self._handler,
            identifier="update_metadata",
            title="Update Metadata",
            abstract="Update NetCDF metadata from a YAML file.",
            version="0.1.0",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True,
        )

    @staticmethod
    def _handler(request, response):
        args = Namespace(
            ncfile=request.inputs['netcdf'][0].file,
            updates=request.inputs['updates'][0].file,
        )

        main(args)
        return response
