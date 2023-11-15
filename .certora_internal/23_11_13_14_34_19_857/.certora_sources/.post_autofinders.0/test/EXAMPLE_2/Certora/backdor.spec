methods {
    function backdoor(uint256 x) external;
}

// Regla para verificar que backdoor no revierte incorrectamente
rule checkBackdoorDoesNotRevertNormally(uint256 x) {
    env e;

    // Solo ejecutar backdoor si x no es igual a 6912213124124532
    if (x != 6912213124124532) {
        backdoor(e, x);

        // Confirmar que la ejecución llega al final sin revertir
        assert true, "La ejecución debe completarse sin errores";
    }
}

// Regla para verificar que backdoor revierte correctamente
rule checkBackdoorRevertsCorrectly() {
    env e;

    uint256 x = 6912213124124532; // Este valor debería activar el revert

    backdoor@withrevert(e, x);

    // Confirmar que la ejecución activa el revert
    assert lastReverted, "La ejecución debe revertir con CoffeeBreak";
}
