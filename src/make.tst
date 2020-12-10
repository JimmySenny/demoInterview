include ../etc/Makefile

BIN_NAME = tst_pufa

OBJ_LIB  = ${WORKDIR}/lib/libtst.a ${WORKDIR}/lib/libcomm.a ${WORKDIR}/lib/libpufa.a

EXECOBJ  = ${WORKDIR}/bin/${BIN_NAME}.out

LINKRULE = ${CC} -o ${EXECOBJ} ${OBJ_LIB} -L${WORKDIR}/lib -ltst -lcomm -lpufa

TARGETS  = ${EXECOBJ}

all:${TARGETS}

${EXECOBJ}: ${OBJ_LIB}
	${LINKRULE}

clean:
	@- rm -f ${TARGETS} ${CLEANFILES}
