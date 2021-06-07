import numpy as np

class Parser:

    show_info = False

    def parse_file(self, file_name: str) -> list:

        file = open(file_name, "r")
        temp_string = file.read()

        return self.parse_string(temp_string)

    ############################################################################################

    def parse_string(self, string_to_parse: str) -> list:

        char_counter = 0
        tab_lang = []

        for a in range(65, 91):
            
            if self.show_info:
                print(chr(a))
            for b in range(65, 91):
                
                doub_char_cnt = 0

                for i in range(0, len(string_to_parse) - 1):

                    fir_c = ord(string_to_parse[i])
                    sec_c = ord(string_to_parse[i+1])

                    if fir_c == a or fir_c == a + 32:
                        if sec_c == b or sec_c == b + 32:

                            doub_char_cnt += 1
                            char_counter += 1

                tab_lang.append(doub_char_cnt)

        final_list = []

        for element in tab_lang:
            final_list.append(element/char_counter)

        return final_list

    ############################################################################################

    def save_weights(self, weights: np.array):

        file = open("SavedWeights.sav", "w")
        for weight in weights:
            
            for element in weight:
                file.write(str(element))
                file.write(" ")
            file.write("\n")
        
        file.close()

    ############################################################################################

    def load_weights(self) -> np.array:

        return np.loadtxt("SavedWeights.sav", dtype=np.float)