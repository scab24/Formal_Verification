methods {
    function backdoor(uint256 x) external;
}

/** @title Verificar que backdoor no revierte para valores de x diferentes de 6912213124124532 */
rule backdoorDoesNotRevertNormally(uint256 x) {
    env e;

    // Asegurar que x no sea el valor que activa la reversión
    require x != 6912213124124532;

    backdoor(e, x);

    // La ejecución debe completarse sin errores
    assert true, "La ejecución debe completarse sin errores";
}

/** @title Verificar que backdoor revierte para el valor 6912213124124532 */
rule backdoorRevertsCorrectly() {
    env e;

    uint256 x = 6912213124124532; // Este valor debería activar el revert

    backdoor@withrevert(e, x);

    assert lastReverted, "La ejecución debe revertir bajo condiciones específicas";
}
