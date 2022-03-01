library ieee;
use ieee.std_logic_1164.all;

entity soma_subtrai4bits is
    port (
        A, B : in std_logic_vector (3 downto 0);  -- 2 numeros de 4 bits
        C : in std_logic_vector (1 downto 0);  -- operacao de soma ou subtrai
        S : out std_logic_vector (3 downto 0);  -- saida de 4 bits
        Overflow : out std_logic  -- permite que a saida tenha 5 bits
    );
end entity;

architecture whatever of soma_subtrai4bits is

    signal modb0, modb1, modb2, modb3 : std_logic;
    signal carry0, carry1, carry2, carry3 : std_logic;

    component modb is
        port (
            C0, C1, B : in std_logic;
            S : out std_logic
        );
    end component;

    component full_adder is
        port (
            A, B, Cin : in std_logic;
            S, Cout : out std_logic
        );
    end component;

begin

    MD0 : modb port map (C(0), C(1), B(0), modb0);
    FA0 : full_adder port map (A(0), modb0, C(0), S(0), carry0);
    
    MD1 : modb port map (C(0), C(1), B(1), modb1);
    FA1 : full_adder port map (A(1), modb1, carry0, S(1), carry1);
    
    MD2 : modb port map (C(0), C(1), B(2), modb2);
    FA2 : full_adder port map (A(2), modb2, carry1, S(2), carry2);
    
    MD3 : modb port map (C(0), C(1), B(3), modb3);
    FA3 : full_adder port map (A(3), modb3, carry2, S(3), carry3);

    Overflow <= carry2 xor carry3;

end architecture;