library ieee;
use ieee.std_logic_1164.all;

entity half_adder is
port(
    SW: in std_logic_vector(1 downto 0);
    LEDR: out std_logic_vector(1 downto 0)
);
end entity;

architecture logic of half_adder is
    signal teste1, teste2: std_logic;
begin
    teste1 <= SW(0) xor SW(1);
    teste2 <= SW(0) and SW(1);
    LEDR(1) <= teste2;
    LEDR(0) <= teste1;
end architecture;
