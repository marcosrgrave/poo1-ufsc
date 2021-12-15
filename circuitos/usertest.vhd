library ieee;
use ieee.std_logic_1164.all;

entity usertest is
    -- entity sem portas p/ testbench
end entity;

architecture sim of usertest is
    signal SA, SB, SSum, SCout : std_logic;
    component halfadder is port(
        A, B : in std_logic;
        Sum, Cout : out std_logic
    );
    end component;
begin
    DUT : halfadder port map(
        -- SA <= A,
        -- SB <= B,
        -- SSum <= Sum,
        -- SCout <= Cout
        A => SA,
        B => SB,
        Sum => SSum,
        Cout => SCout
    )
    SA <= '0', '1' after 20 ns, '0' after 40 ns;
    --  SA recebe 0 inicialmente e depois de 20 nano segundos, recebe 1, e etc.
    -- esse 'after'só serve para testbench, nao para projeto.
    SB <= '0', '1' after 10 ns, '0' after 20 ns, '1' after 30 ns;
end architecture;