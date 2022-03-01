-- Libraries and Packages (IEEE)
library ieee;
use ieee.std_logic_1164.all;

-- Entity (Ports)
entity somador4bits is
    port (
        A, B : in std_logic_vector (3 downto 0);  -- 2 numeros de 4 bits que serao somados
        S : out std_logic_vector (4 downto 0)  -- a soma pode resultar em um numero de até 5 bits
    );
end entity;

-- Architecture (Comportamento/Funcionalidade)
architecture rtl of somador4bits is
    
    signal carry0, carry1, carry2 : std_logic;  -- os 'carrys' podem ser 0 ou 1

    component half_adder is
        port(  -- as portas devem ser iguais às portas do código original
            A, B : in std_logic;
            S, Cout : out std_logic
        );
    end component;

    component full_adder is
        port(  -- as portas devem ser iguais às portas do código original
            A, B, Cin : in std_logic;
            S, Cout : out std_logic
        );
    end component;

begin  -- aqui começa a utilização dos código importados pelo comando 'component'
    
    HALF0 : half_adder port map (  -- ORDEM: codigo_ja_feito => codigo_atual
        A => A(0),
        B => B(0),
        S => S(0),
        Cout => carry0
    );

    FULL1 : full_adder port map(
        A => A(1),
        B => B(1),
        Cin => carry0,
        S => S(1),
        Cout => carry1
    );

    FULL2 : full_adder port map(
        A => A(2),
        B => B(2),
        Cin => carry1,
        S => S(2),
        Cout => carry2
    );

    FULL3 : full_adder port map(
        A => A(3),
        B => B(3),
        Cin => carry2,
        S => S(3),
        Cout => S(4)
    );

end architecture;