import sys

def get_i_p_list(preference_list, num):
    i_p_list = [0 for i in range(num)]
    for i in range(num):
        i_p_list[preference_list[i]] = i
    return i_p_list

def get_first_w(m_prefrence_list, m_id):
    w = m_prefrence_list[m_id]
    while len(w) != 0:
        w_id = w.pop(0)
        return w_id
  
while(True):
    m_prefrence_list = []
    inverse_w_p_list = []
    m_list = []
    husband = []
    wife = []
    inputs = sys.stdin.readline().strip()
    if inputs[0] != "#":
        content = inputs.split(" ")
        num_of_pair = int(content[2])
        m_list = [int(i) for i in range(num_of_pair)]
        husband = [None for i in range(num_of_pair)]
        wife = [None for i in range(num_of_pair)]
        for i in range(int(num_of_pair)* 2 + 1):
            inputs = sys.stdin.readline().strip()
            if inputs[0] != "#":
                inputs = inputs.split(":")
                num = inputs[0]
                preference = inputs[1].strip().split(" ")
                if int(num) % 2 == 1:
                    preference_list = [int(int(i)/2) - 1 for i in preference]
                    m_prefrence_list.append(preference_list)
                else:
                    preference_list = [int((int(i)- 1)/2) for i in preference]
                    i_p_list = get_i_p_list(preference_list, int(num_of_pair))
                    inverse_w_p_list.append(i_p_list)
                    
        while len(m_list) != 0:
            m_id = m_list.pop(0)
            w_id = get_first_w(m_prefrence_list, m_id)

            if husband[w_id] == None:
                wife[m_id] = w_id
                husband[w_id] = m_id
            else:
                original_m = husband[w_id]
                if inverse_w_p_list[w_id][original_m] < inverse_w_p_list[w_id][m_id]:
                    m_list.append(m_id)
                else:
                    wife[m_id] = w_id
                    husband[w_id] = m_id
                    m_list.append(original_m)
                    
        for i in range(int(num_of_pair)):
            print( i * 2 + 1, (wife[i] + 1)* 2)
        break 
