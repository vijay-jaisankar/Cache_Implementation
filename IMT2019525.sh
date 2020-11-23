# IMT2019525 VIJAY JAISANKAR

# Colour Coding
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m' 
RED='\033[1;31m' 

printf "${RED}Done By: IMT2019525 VIJAY JAISANKAR${NC} \n\n"

printf "${YELLOW}Direct Mapped Cache${NC} \n"
# Executing the files
printf "${BLUE}File name : gcc.trace${NC} \n"
python3 direct_mapped_cache.py -f "traces/gcc.trace"
printf "${BLUE}File name : gzip.trace${NC} \n"
python3 direct_mapped_cache.py -f "traces/gzip.trace"
printf "${BLUE}File name : mcf.trace${NC} \n"
python3 direct_mapped_cache.py -f "traces/mcf.trace"
printf "${BLUE}File name : swim.trace${NC} \n"
python3 direct_mapped_cache.py -f "traces/swim.trace"
printf "${BLUE}File name : twolf.trace${NC} \n"
python3 direct_mapped_cache.py -f "traces/twolf.trace"

printf "${YELLOW}Set Associative Cache${NC} \n"
# Executing the files
printf "${BLUE}File name : gcc.trace${NC} \n"
python3 set_associative_cache.py -f "traces/gcc.trace"
printf "${BLUE}File name : gzip.trace${NC} \n"
python3 set_associative_cache.py -f "traces/gzip.trace"
printf "${BLUE}File name : mcf.trace${NC} \n"
python3 set_associative_cache.py -f "traces/mcf.trace"
printf "${BLUE}File name : swim.trace${NC} \n"
python3 set_associative_cache.py -f "traces/swim.trace"
printf "${BLUE}File name : twolf.trace${NC} \n"
python3 set_associative_cache.py -f "traces/twolf.trace"


