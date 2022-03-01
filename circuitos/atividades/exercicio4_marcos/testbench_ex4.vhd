library ieee;
use ieee.std_logic_1164.all;

entity testbench_ex4 is
end entity;

architecture tb of testbench_ex4 is

 signal clk, Rtest, Btest : std_logic := '0';
 signal Stest: std_logic_vector(1 downto 0);

 component FSM1 is port (
 CLK : in std_logic;
 CLR : in std_logic;
 B: in std_logic;
 S: out std_logic_vector(1 downto 0)
 );
 end component;

begin

 myfsm: FSM1 port map (clk, Rtest, Btest, Stest);

 clk <= not clk after 5 ns;
 Rtest <= '1', '0' after 15 ns;
 Btest <= '0', '1' after 25 ns, '0' after 40 ns, '1' after 122 ns, '0' after 135 ns;

end tb;