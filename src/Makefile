include ../etc/Makefile

ALLDIRS = ${WORKDIR}/src/comm \
		  ${WORKDIR}/src/pufa \
		  ${WORKDIR}/src/tst 

all:
	@for subdir in ${ALLDIRS}; \
	do \
		cd $$subdir;\
		echo "Makeing $$subdir"; \
		${MAKE} ${MAKEOPT} all; \
		echo " Done "; \
	done

clean:
	@for subdir in ${ALLDIRS}; \
	do \
		cd $$subdir;\
		echo "Cleaning $$subdir"; \
		${MAKE} ${MAKEOPT} clean; \
		echo " Done "; \
	done
