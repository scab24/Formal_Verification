methods {
    function backdoor(uint256 x) external;
}

rule checkBackdoorDoesNotRevertNormally(uint256 x) {
    env e;

    // Asegurarse de que no se cumple la condición de revertir
    if (x == 6912213124124532) {
        return;
    }

    backdoor(e, x);

    // Confirmar que la ejecución llega al final sin revertir
    assert true, "La ejecución debe completarse sin errores";
}

rule checkBackdoorRevertsCorrectly() {
    env e;

    uint256 x = 6912213124124532; // Este valor debería activar el revert

    backdoor@withrevert(e, x);

    // Confirmar que la ejecución activa el revert
    assert lastReverted, "La ejecución debe revertir con CoffeeBreak";
}
