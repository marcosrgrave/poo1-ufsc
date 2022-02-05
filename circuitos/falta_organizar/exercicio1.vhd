library IEEE;
use IEEE.Std_Logic_1164.all;

entity exercicio1 is
port (A: in std_logic;  -- podia ser simplesmente:
      B: in std_logic;  -- A, B, C, D : in std_logic;
      C: in std_logic;  -- W, X, Y, Z : out std_logic;
      D: in std_logic;
      W: out std_logic;
      X: out std_logic;
      Y: out std_logic;
      Z: out std_logic
	);
end exercicio1;

architecture logica of exercicio1 is
begin
    
    W <= (A and not B and not C) or (C and not D) or (not A and B) or (not A and C);
    X <= (B and not C and not D) or (A and not C and not D) or (not A and not C and D);
    Y <= (A and not B and D) or (not B and C);
    Z <= (C and not D) or (not B and not C) or not A;
    
end logica;
