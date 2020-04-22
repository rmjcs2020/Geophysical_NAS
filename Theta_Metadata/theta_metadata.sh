#! /bin/sh

# Linux data-gathering commands; adjust as necessary for your platform.
#
# Be sure to remove any information from the output that would violate
# SC's double-blind review policies.

#COBALT -n 1
#COBALT -t 00:10:00
#COBALT -q debug-cache-quad 
#COBALT -A datascience

#Loading modules
export PATH=/soft/datascience/anaconda3/bin:$PATH
export PATH=/soft/libraries/mpi/mvapich2/gcc/bin/:$PATH
source /NAS_PINN/NAS_PINN_Env/bin/activate
source balsamactivate NAS_PINN_db

aprun -n 1 -N 1 ./sc_data.sh


