library ieee;
use ieee.std_logic_1164.all;

entity majority_detector is
port(
    A: in std_logic;
    B: in std_logic;
    C: in std_logic;
    Y: out std_logic
);
end entity;

architecture arc of majority_detector is
    signal LG1, LG2, LG3: std_logic;
begin
    LG1 <= A and B;
    LG2 <= A and C;
    LG3 <= B and C;
    Y <= LG1 or LG2 or LG3;
end architecture;
