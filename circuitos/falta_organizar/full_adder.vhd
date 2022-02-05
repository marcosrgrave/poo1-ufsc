library ieee;
use ieee.std_logic_1164.all;

entity full_adder is
port(
    SW: in std_logic_vector(2 downto 0);
    LEDR: out std_logic_vector(1 downto 0)
);
end entity;

architecture logic of full_adder is
    signal A, B, Cin, txor1, tand1, tand2, txor2, tor, S, Cout: std_logic;
begin
    A <= SW(0);
    B <= SW(1);
    Cin <= SW(2);
    LEDR(0) <= S;
    LEDR(1) <= Cout;
    
    txor1 <= A xor B;
    txor2 <= txor1 xor Cin;
    tand1 <= txor1 and Cin;
    tand2 <= B and Cin;
    tor <= tand1 or tand2;
    
    S <= txor2;
    Cout <= tor;
end architecture;
