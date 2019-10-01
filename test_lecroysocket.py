#  
# dsopy-lecroy
# Copyright (C) 2019 Sunghyun Jin
# 
# based on
#  
# LeCrunch2 
# Copyright (C) 2014 Benjamin Land
#
# based on
#
# LeCrunch
# Copyright (C) 2010 Anthony LaTorre 
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import matplotlib.pyplot as plt
from lecroysocket import LeCroyScope

ip = '163.152.90.101'

dso = LeCroyScope(ip, timeout=5)
dso.clear()
settings = dso.get_settings()
#print(settings)
print('settings')
for k in settings.keys():
    print(k, ':', settings[k])
channels = dso.get_channels()
print(channels)

desc2, rw2 = dso.get_waveform(2)
desc3, rw3 = dso.get_waveform(3)

plt.plot(rw2)
plt.plot(rw3)
plt.show()

