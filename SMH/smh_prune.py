#!/usr/bin/env python
# -*- coding: utf-8
#
# Gibran Fuentes-Pineda <gibranfp@unam.mx>
# IIMAS, UNAM
# 2018
#
# -------------------------------------------------------------------------
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
# -------------------------------------------------------------------------
"""
Adds pruning to SMHDiscoverer class
"""
from smh import ListDB, SMHDiscoverer
import smh_api as sa

class SMHD(SMHDiscoverer):
    def fit(self,
            listdb,
            prune = True,
            weights = None,
            expand = None):
        """
        Discovers patterns from a database of lists
        """
        mined = self.mine(listdb, weights = weights, expand = expand)
        if prune:
            sa.sampledmh_prune(listdb.ldb,mined.ldb,3,3,0.7,0.8)
        models = sa.mhlink_cluster(mined.ldb,
                                   self.cluster_tuple_size_,
                                   self.cluster_number_of_tuples_,
                                   self.cluster_table_size_,
                                   sa.list_overlap,
                                   self.overlap_,
                                   self.min_cluster_size_)
        sa.listdb_apply_to_all(models, sa.list_sort_by_frequency_back)

        mined.destroy()

        return ListDB(ldb = models)
        
