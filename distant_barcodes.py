import heapq

class Solution(object):

    def rearrangeBarcodes(self, barcodes):
        freq_map = {}
        for barcode in barcodes:
            if barcode in freq_map:
                freq_map[barcode] += 1
            else:
                freq_map[barcode] = 1

        result = []

        max_heap = [(-freq, barcode) for barcode, freq in freq_map.items()]
        heapq.heapify(max_heap)
        prev_freq, prev_barcode = 0, None

        while max_heap:
            freq, barcode = heapq.heappop(max_heap)
            result.append(barcode)
            freq += 1

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_barcode))

            prev_freq, prev_barcode = freq, barcode

        return result
