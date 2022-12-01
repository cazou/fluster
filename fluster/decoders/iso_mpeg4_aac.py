# Fluster - testing framework for decoders conformance
# Copyright (C) 2021, Fluendo, S.A.
#  Author: Michalis Dimopoulos <mdimopoulos@fluendo.com>, Fluendo, S.A.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <https://www.gnu.org/licenses/>.

from fluster.codec import Codec, OutputFormat
from fluster.decoder import Decoder, register_decoder
from fluster.utils import file_checksum, run_command


@register_decoder
class ISOAACDecoder(Decoder):
    '''ISO MPEG4 AAC reference decoder implementation'''
    name = "ISO-MPEG4-AAC"
    description = "ISO MPEG4 AAC reference decoder"
    codec = Codec.AAC
    binary = 'mp4audec_mc'

    def decode(self, input_filepath: str, output_filepath: str, output_format: OutputFormat, timeout: int,
               verbose: bool, keep_files: bool) -> str:
        '''Decodes input_filepath in output_filepath'''
        # pylint: disable=unused-argument
        # Addition of .pcm as extension is a must. If it is something else, e.g. ".out" the decoder will output a
        # ".wav", which is undesirable.
        output_filepath += ".pcm"
        run_command([self.binary, input_filepath, output_filepath],
                    timeout=timeout, verbose=verbose)
        return file_checksum(output_filepath)
