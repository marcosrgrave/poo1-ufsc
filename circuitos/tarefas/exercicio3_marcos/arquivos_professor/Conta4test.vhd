library ieee;
use ieee.std_logic_1164.all;

entity Conta4test is
end Conta4test;

architecture tb of Conta4test is

-- Declaração dos sinais do testbench:
 signal CLRtest: std_logic;
 signal CLKtest: std_logic := '0';
 signal Stest: std_logic_vector(3 downto 0);
 
 -- Declaração do componente a ser testado:
 component Conta4 is port ( 
 CLK: in std_logic;
 CLR: in std_logic;
 S: out std_logic_vector(3 downto 0) );
 end component;

begin

 -- Criando instância do componente a ser testado:
 DUT : Conta4 port map (CLK => CLKtest, CLR => CLRtest, S => Stest);
 -- Estímulos:
 CLKtest <= not CLKtest after 5 ns; -- Geração de clock com período de 10 ns.
 CLRtest <= '1', '0' after 20 ns; -- Estimulando o CLR (inicialmente em '1' e vira '0' depois de 20 ns).

end tb;